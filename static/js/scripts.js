/**
 * Internship Form Portal - Client-side scripts
 * This file contains JavaScript functionality for enhancing the user experience
 * with form validation, printing, and interactive elements.
 */

document.addEventListener('DOMContentLoaded', function() {
    // Initialize all interactive elements
    initFormValidation();
    initPrintButtons();
    initDatePickers();
    initPdfButtons();
    
    // Flash message auto-hide after 5 seconds
    setTimeout(function() {
        const flashMessages = document.querySelectorAll('.flash-message');
        flashMessages.forEach(function(message) {
            message.style.opacity = '0';
            setTimeout(function() {
                message.style.display = 'none';
            }, 500);
        });
    }, 5000);
});

/**
 * Initialize client-side form validation for the internship form
 * This enhances the server-side validation by providing immediate feedback
 */
function initFormValidation() {
    const form = document.querySelector('.internship-form');
    
    if (!form) return; // Exit if form doesn't exist on this page
    
    // Add validation for required fields
    form.addEventListener('submit', function(event) {
        let isValid = true;
        
        // Check all required inputs
        const requiredInputs = form.querySelectorAll('input[required], textarea[required], select[required]');
        requiredInputs.forEach(function(input) {
            if (!input.value.trim()) {
                isValid = false;
                highlightInvalidField(input);
            } else {
                resetFieldHighlight(input);
            }
        });
        
        // Check email field format if it exists and has a value
        const emailField = form.querySelector('input[type="email"]');
        if (emailField && emailField.value.trim()) {
            if (!isValidEmail(emailField.value.trim())) {
                isValid = false;
                highlightInvalidField(emailField);
            } else {
                resetFieldHighlight(emailField);
            }
        }
        
        // If validation fails, prevent form submission
        if (!isValid) {
            event.preventDefault();
            showValidationErrorMessage();
            scrollToFirstError();
        }
    });
    
    // Add input event listeners to clear error state when user starts typing
    const allInputs = form.querySelectorAll('input, textarea, select');
    allInputs.forEach(function(input) {
        input.addEventListener('input', function() {
            resetFieldHighlight(this);
        });
    });
}

/**
 * Validate email format
 * @param {string} email - Email address to validate
 * @returns {boolean} True if email format is valid
 */
function isValidEmail(email) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
}

/**
 * Highlight an invalid form field
 * @param {HTMLElement} field - The field to highlight
 */
function highlightInvalidField(field) {
    field.classList.add('invalid-field');
    
    // Add error message if it doesn't exist
    let errorContainer = field.parentNode.querySelector('.client-validation-error');
    if (!errorContainer) {
        errorContainer = document.createElement('div');
        errorContainer.className = 'client-validation-error error-message';
        errorContainer.textContent = field.hasAttribute('data-error-message') 
            ? field.getAttribute('data-error-message') 
            : 'This field is required';
        field.parentNode.appendChild(errorContainer);
    }
}

/**
 * Reset highlighting on a form field
 * @param {HTMLElement} field - The field to reset
 */
function resetFieldHighlight(field) {
    field.classList.remove('invalid-field');
    
    // Remove error message if it exists
    const errorContainer = field.parentNode.querySelector('.client-validation-error');
    if (errorContainer) {
        errorContainer.remove();
    }
}

/**
 * Show a validation error message at the top of the form
 */
function showValidationErrorMessage() {
    // Check if error message already exists
    let errorMessage = document.querySelector('.form-validation-error');
    if (!errorMessage) {
        errorMessage = document.createElement('div');
        errorMessage.className = 'flash-message flash-error form-validation-error';
        errorMessage.textContent = 'Please correct the errors in the form before submitting.';
        
        const form = document.querySelector('.internship-form');
        form.parentNode.insertBefore(errorMessage, form);
    }
}

/**
 * Scroll to the first error in the form
 */
function scrollToFirstError() {
    const firstError = document.querySelector('.invalid-field');
    if (firstError) {
        firstError.scrollIntoView({ behavior: 'smooth', block: 'center' });
    }
}

/**
 * Initialize print functionality for print buttons
 * Enhanced to provide better print experience for A4 paper
 */
function initPrintButtons() {
    const printButtons = document.querySelectorAll('button[onclick="window.print()"]');
    
    printButtons.forEach(function(button) {
        button.addEventListener('click', function(event) {
            // Add any pre-print preparations here if needed
            prepareForPrinting();
            
            // Use the browser's print functionality
            window.print();
            
            // Restore any changes made for printing
            restoreAfterPrinting();
        });
    });
}

/**
 * Prepare the page for printing
 * This function makes any necessary DOM adjustments before printing
 * Optimized for A4 paper format
 */
function prepareForPrinting() {
    // Add 'printing' class to body for print-specific styling
    document.body.classList.add('printing');
    
    // Hide elements with 'no-print' class
    const noPrintElements = document.querySelectorAll('.no-print');
    noPrintElements.forEach(function(element) {
        element.setAttribute('data-print-display', element.style.display);
        element.style.display = 'none';
    });

    // Additional preparation for optimal A4 layout
    // The CSS will handle most of this through @media print rules
    console.log('Preparing document for A4 print format');
}

/**
 * Restore the page after printing
 * This function reverses any DOM changes made for printing
 */
function restoreAfterPrinting() {
    // Remove 'printing' class from body
    document.body.classList.remove('printing');
    
    // Restore display of 'no-print' elements
    const noPrintElements = document.querySelectorAll('.no-print');
    noPrintElements.forEach(function(element) {
        if (element.hasAttribute('data-print-display')) {
            element.style.display = element.getAttribute('data-print-display');
            element.removeAttribute('data-print-display');
        } else {
            element.style.display = '';
        }
    });

    console.log('Print preparation restored');
}

/**
 * Initialize date pickers for date input fields
 * This provides a fallback for browsers that don't support the date input type
 */
function initDatePickers() {
    // Check if the browser supports date inputs
    const testInput = document.createElement('input');
    testInput.type = 'date';
    const isDateSupported = testInput.type === 'date';
    
    // If date inputs are not supported, we could add a polyfill or third-party date picker here
    if (!isDateSupported) {
        console.log('Date input not supported by browser. Consider adding a date picker library.');
        
        // Example implementation would go here if we decide to add a datepicker library
        // This is left as a placeholder for future enhancement
    }
}

/**
 * Initialize PDF download and print buttons
 */
function initPdfButtons() {
    // Initialize PDF download buttons
    const pdfDownloadLinks = document.querySelectorAll('.btn-download');
    
    pdfDownloadLinks.forEach(function(link) {
        link.addEventListener('click', function(event) {
            // Show a loading indicator if the download might take time
            const loadingIndicator = document.createElement('span');
            loadingIndicator.className = 'loading-indicator';
            loadingIndicator.textContent = ' Loading...';
            link.appendChild(loadingIndicator);
            
            // Remove the loading indicator after 2 seconds (typical download start time)
            setTimeout(function() {
                link.removeChild(loadingIndicator);
            }, 2000);
        });
    });
    
    // Initialize PDF print buttons
    const pdfPrintButtons = document.querySelectorAll('.btn-print');
    
    pdfPrintButtons.forEach(function(button) {
        // If the button doesn't already have an onclick handler for printPDF function
        if (!button.getAttribute('onclick') || !button.getAttribute('onclick').includes('printPDF')) {
            button.addEventListener('click', function(event) {
                const formId = button.getAttribute('data-form-id');
                if (formId) {
                    printPDF(formId);
                } else {
                    console.error('No form ID specified for PDF printing');
                }
            });
        }
    });
}

/**
 * Print a PDF by loading it in an iframe
 * @param {string|number} formId - ID of the form to print the PDF for
 */
function printPDF(formId) {
    // Show loading indicator
    const loadingOverlay = document.createElement('div');
    loadingOverlay.className = 'loading-overlay';
    loadingOverlay.innerHTML = '<div class="loading-spinner"></div><p>Preparing PDF for printing...</p>';
    document.body.appendChild(loadingOverlay);
    
    // Convert formId to number if it's a string
    const numericId = typeof formId === 'string' ? parseInt(formId, 10) : formId;
    
    // Fetch the PDF
    fetch(`/download_pdf/${numericId}`, {
        method: 'GET'
    })
    .then(response => response.blob())
    .then(blob => {
        // Remove loading overlay
        document.body.removeChild(loadingOverlay);
        
        // Create a temporary URL for the PDF
        const url = window.URL.createObjectURL(blob);
        
        // Create an iframe to hold the PDF for printing
        const printFrame = document.createElement('iframe');
        printFrame.style.position = 'fixed';
        printFrame.style.right = '0';
        printFrame.style.bottom = '0';
        printFrame.style.width = '0';
        printFrame.style.height = '0';
        printFrame.style.border = '0';
        
        // When the iframe loads, print its contents
        printFrame.onload = function() {
            setTimeout(function() {
                printFrame.contentWindow.print();
                
                // Clean up after printing
                setTimeout(function() {
                    document.body.removeChild(printFrame);
                    window.URL.revokeObjectURL(url);
                }, 1000);
            }, 500);
        };
        
        // Set the source and add the iframe to the document
        printFrame.src = url;
        document.body.appendChild(printFrame);
    })
    .catch(error => {
        // Remove loading overlay
        document.body.removeChild(loadingOverlay);
        
        console.error('Error printing PDF:', error);
        alert('Could not print the PDF. Please try downloading it instead.');
    });
}

/**
 * Preview a form as PDF before submission
 * This function is called from the form page
 */
function previewFormAsPDF() {
    const form = document.getElementById('internship-form');
    if (!form) {
        console.error('Form not found for PDF preview');
        return;
    }
    
    const formData = new FormData(form);
    
    // Show the modal with loading message
    const modal = document.getElementById('pdfPreviewModal');
    const previewContainer = document.getElementById('pdfPreviewContainer');
    
    if (!modal || !previewContainer) {
        console.error('PDF preview modal elements not found');
        return;
    }
    
    modal.style.display = 'block';
    previewContainer.innerHTML = '<div class="loading-spinner"></div><p>Generating PDF preview...</p>';
    
    // Send form data to server for PDF generation
    fetch('/preview_pdf', {
        method: 'POST',
        body: formData
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('PDF preview generation failed');
        }
        return response.text();
    })
    .then(() => {
        // Load the generated PDF in an iframe
        const iframe = document.createElement('iframe');
        iframe.src = '/preview_pdf';
        iframe.style.width = '100%';
        iframe.style.height = '100%';
        iframe.style.border = 'none';
        
        // Clear container and add iframe
        previewContainer.innerHTML = '';
        previewContainer.appendChild(iframe);
    })
    .catch(error => {
        console.error('Error generating PDF preview:', error);
        previewContainer.innerHTML = '<p style="color: red;">Error generating PDF preview. Please try again or submit the form to see the final PDF.</p>';
    });
} 