/**
 * Internship Form Portal - Client-side scripts
 * This file contains JavaScript functionality for enhancing the user experience
 * with form validation, printing, and interactive elements.
 */

document.addEventListener('DOMContentLoaded', function() {
    // Initialize all interactive elements
    initFormValidation();
    initFormToggleControls();
    initFormSubmitInteractivity();
    
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
 * Initialize form toggle controls
 */
function initFormToggleControls() {
    // Implementation of initFormToggleControls function
}

/**
 * Initialize form submit interactivity
 */
function initFormSubmitInteractivity() {
    // Implementation of initFormSubmitInteractivity function
} 