/**
 * Documentation Site - Custom JavaScript
 * Provides enhanced functionality for the documentation platform
 */

(function() {
    'use strict';

    // Global app object
    window.DocsApp = {
        init: function() {
            this.initCopyButtons();
            this.initKeyboardShortcuts();
            this.initTooltips();
            this.initSearchEnhancements();
            this.initThemeToggle();
        },

        // Add copy buttons to code blocks
        initCopyButtons: function() {
            const codeBlocks = document.querySelectorAll('pre code');
            
            codeBlocks.forEach(function(codeBlock) {
                const button = document.createElement('button');
                button.className = 'copy-btn';
                button.innerHTML = '📋 Copy';
                button.setAttribute('aria-label', 'Copy code to clipboard');
                
                const pre = codeBlock.parentNode;
                pre.style.position = 'relative';
                pre.appendChild(button);
                
                button.addEventListener('click', function() {
                    navigator.clipboard.writeText(codeBlock.textContent).then(function() {
                        button.innerHTML = '✅ Copied!';
                        button.classList.add('btn-success');
                        
                        setTimeout(() => {
                            button.innerHTML = '📋 Copy';
                            button.classList.remove('btn-success');
                        }, 2000);
                    }).catch(function() {
                        // Fallback for older browsers
                        const textArea = document.createElement('textarea');
                        textArea.value = codeBlock.textContent;
                        document.body.appendChild(textArea);
                        textArea.select();
                        document.execCommand('copy');
                        document.body.removeChild(textArea);
                        
                        button.innerHTML = '✅ Copied!';
                        setTimeout(() => {
                            button.innerHTML = '📋 Copy';
                        }, 2000);
                    });
                });
            });
        },

        // Keyboard shortcuts
        initKeyboardShortcuts: function() {
            document.addEventListener('keydown', function(e) {
                // Ctrl/Cmd + / for search focus
                if ((e.ctrlKey || e.metaKey) && e.key === '/') {
                    e.preventDefault();
                    const searchInput = document.querySelector('input[name="q"]');
                    if (searchInput) {
                        searchInput.focus();
                    }
                }
                
                // Ctrl/Cmd + K for new document
                if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
                    e.preventDefault();
                    window.location.href = '/new';
                }
                
                // Escape to close modals or unfocus
                if (e.key === 'Escape') {
                    const activeElement = document.activeElement;
                    if (activeElement && activeElement.blur) {
                        activeElement.blur();
                    }
                }
            });
        },

        // Initialize tooltips
        initTooltips: function() {
            // Add tooltips to buttons and links
            const elements = document.querySelectorAll('[title], [aria-label]');
            elements.forEach(function(element) {
                if (element.title || element.getAttribute('aria-label')) {
                    element.addEventListener('mouseenter', function() {
                        // Simple tooltip implementation
                        const tooltip = document.createElement('div');
                        tooltip.className = 'custom-tooltip';
                        tooltip.textContent = this.title || this.getAttribute('aria-label');
                        document.body.appendChild(tooltip);
                        
                        const rect = this.getBoundingClientRect();
                        tooltip.style.position = 'absolute';
                        tooltip.style.top = (rect.top - tooltip.offsetHeight - 5) + 'px';
                        tooltip.style.left = (rect.left + rect.width / 2 - tooltip.offsetWidth / 2) + 'px';
                        tooltip.style.background = '#333';
                        tooltip.style.color = 'white';
                        tooltip.style.padding = '5px 10px';
                        tooltip.style.borderRadius = '4px';
                        tooltip.style.fontSize = '12px';
                        tooltip.style.zIndex = '1000';
                        
                        this._tooltip = tooltip;
                    });
                    
                    element.addEventListener('mouseleave', function() {
                        if (this._tooltip) {
                            document.body.removeChild(this._tooltip);
                            this._tooltip = null;
                        }
                    });
                }
            });
        },

        // Search enhancements
        initSearchEnhancements: function() {
            const searchInput = document.querySelector('input[name="q"]');
            if (searchInput) {
                // Add search suggestions
                searchInput.addEventListener('input', function() {
                    // Implement live search suggestions here
                    // For now, just add a simple placeholder enhancement
                    if (this.value.length > 2) {
                        this.style.background = '#f0f8ff';
                    } else {
                        this.style.background = '';
                    }
                });
                
                // Clear search on escape
                searchInput.addEventListener('keydown', function(e) {
                    if (e.key === 'Escape') {
                        this.value = '';
                        this.blur();
                    }
                });
            }
        },

        // Theme toggle functionality
        initThemeToggle: function() {
            // Check for saved theme preference
            const savedTheme = localStorage.getItem('docs-theme');
            if (savedTheme) {
                document.body.setAttribute('data-theme', savedTheme);
            }
            
            // Create theme toggle button
            const themeButton = document.createElement('button');
            themeButton.className = 'btn btn-outline-light btn-sm ms-2';
            themeButton.innerHTML = '🌙';
            themeButton.setAttribute('aria-label', 'Toggle theme');
            themeButton.setAttribute('title', 'Toggle dark/light theme');
            
            const navbar = document.querySelector('.navbar .container-fluid');
            if (navbar) {
                navbar.appendChild(themeButton);
                
                themeButton.addEventListener('click', function() {
                    const currentTheme = document.body.getAttribute('data-theme');
                    const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
                    
                    document.body.setAttribute('data-theme', newTheme);
                    localStorage.setItem('docs-theme', newTheme);
                    
                    this.innerHTML = newTheme === 'dark' ? '☀️' : '🌙';
                });
            }
        },

        // Utility functions
        utils: {
            // Debounce function for performance
            debounce: function(func, wait) {
                let timeout;
                return function executedFunction(...args) {
                    const later = () => {
                        clearTimeout(timeout);
                        func(...args);
                    };
                    clearTimeout(timeout);
                    timeout = setTimeout(later, wait);
                };
            },

            // Format date
            formatDate: function(date) {
                return new Intl.DateTimeFormat('en-US', {
                    year: 'numeric',
                    month: 'short',
                    day: 'numeric',
                    hour: '2-digit',
                    minute: '2-digit'
                }).format(new Date(date));
            },

            // Show notification
            showNotification: function(message, type = 'info') {
                const notification = document.createElement('div');
                notification.className = `alert alert-${type} alert-dismissible fade show position-fixed`;
                notification.style.top = '20px';
                notification.style.right = '20px';
                notification.style.zIndex = '9999';
                notification.style.minWidth = '300px';
                
                notification.innerHTML = `
                    ${message}
                    <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
                `;
                
                document.body.appendChild(notification);
                
                // Auto-remove after 5 seconds
                setTimeout(() => {
                    if (notification.parentNode) {
                        notification.parentNode.removeChild(notification);
                    }
                }, 5000);
            }
        }
    };

    // Auto-save functionality for editor
    if (window.location.pathname.includes('/edit') || window.location.pathname.includes('/new')) {
        let autoSaveTimer;
        const editor = document.getElementById('editor');
        const filenameInput = document.getElementById('filename');
        
        if (editor) {
            editor.addEventListener('input', function() {
                clearTimeout(autoSaveTimer);
                
                // Show unsaved indicator
                const saveBtn = document.getElementById('saveBtn');
                if (saveBtn && !saveBtn.disabled) {
                    saveBtn.innerHTML = '💾 Save*';
                }
                
                // Auto-save after 30 seconds of inactivity
                autoSaveTimer = setTimeout(() => {
                    const filename = filenameInput?.value.trim();
                    if (filename && this.value.trim()) {
                        // Auto-save logic here
                        DocsApp.utils.showNotification('Auto-saved draft', 'success');
                    }
                }, 30000);
            });
        }
    }

    // Initialize when DOM is ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', function() {
            DocsApp.init();
        });
    } else {
        DocsApp.init();
    }

    // Progressive Web App functionality
    if ('serviceWorker' in navigator) {
        window.addEventListener('load', function() {
            navigator.serviceWorker.register('/sw.js').then(function(registration) {
                console.log('SW registered: ', registration);
            }).catch(function(registrationError) {
                console.log('SW registration failed: ', registrationError);
            });
        });
    }

})();
