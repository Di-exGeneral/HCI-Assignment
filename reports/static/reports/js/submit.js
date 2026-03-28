const form = document.querySelector('form');
const nameInput = document.querySelector('input[name="name"]');
const phoneInput = document.querySelector('input[name="phone"]');
const descInput = document.querySelector('textarea[name="description"]');
const photoInput = document.querySelector('input[name="photo"]');
const faultTypeInput = document.querySelector('select[name="fault_type"]');


function setError(input) {
    if (input.tagName === 'SELECT') {
        input.classList.add('error');
    } else {
        input.style.borderColor = '#E24B4A';
        input.style.background = '#FCEBEB';
    }
}

function clearError(input) {
    if (input.tagName === 'SELECT') {
        input.classList.remove('error');
    } else {
        input.style.borderColor = '#0F6E56';
        input.style.background = '#ffffff';
    }
}


nameInput.addEventListener('blur', function() {
    if (this.value.trim() === '') {
        setError(this);
    } else {
        clearError(this);
    }
});

phoneInput.addEventListener('blur', function() {
    const phonePattern = /^\d{10}$/;
    if (!phonePattern.test(this.value.trim())) {
        setError(this);
    } else {
        clearError(this);
    }
});

faultTypeInput.addEventListener('change', function() {
    if (this.value === '') {
        setError(this);
    } else {
        clearError(this);
    }
});

descInput.addEventListener('blur', function() {
    if (this.value.trim() === '') {
        setError(this);
    } else {
        clearError(this);
    }
});

photoInput.addEventListener('blur', function() {
    if (this.files.length === 0) {
        setError(this);
    } else {
        clearError(this);
    }
});

form.addEventListener('submit', function(e) {
    e.preventDefault();

    const phonePattern = /^\d{10}$/;

    if (nameInput.value.trim() === '') { setError(nameInput); return; }
    if (!phonePattern.test(phoneInput.value.trim())) { setError(phoneInput); return; }
    if (descInput.value.trim() === '') { setError(descInput); return; }
    if (photoInput.files.length === 0) { setError(photoInput); return; }
    if (faultTypeInput.value === '') { setError(faultTypeInput); return; }
    const confirmed = confirm('Are you sure you want to submit this report?');
    if (!confirmed) return;

    form.submit();
   // alert('Your report has been submitted. You will receive a reference number shortly.');
});
