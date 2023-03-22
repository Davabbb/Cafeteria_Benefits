const uploadForm = document.getElementById('fileUploadForm');
  const fileInput = document.getElementById('receiptFile');
  const fileButton = document.querySelector('.btnfile');
  const submitButton = document.getElementById('submitBtn');

  // show the file input element when the user clicks the file button
  fileButton.addEventListener('click', () => {
    fileInput.click();
  });

  // simulate a click on the submit button when a file is selected
  fileInput.addEventListener('change', () => {
    if (fileInput.files.length > 0) {
      submitButton.click();
    }
  });

  // submit the form when the hidden submit button is clicked
  submitButton.addEventListener('click', () => {
    uploadForm.submit();
  });