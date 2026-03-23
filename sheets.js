function uploadPDF() {
    const fileInput = document.getElementById("pdfInput");
    const output = document.getElementById("output");

    if (fileInput.files.length === 0) {
        output.innerText = "Please select a PDF file.";
        return;
    }

    const file = fileInput.files[0];
    const formData = new FormData();
    formData.append("file", file);

    fetch("http://127.0.0.1:8000/upload-pdf/", {
        method: "POST",
        body: formData
    })
    .then(async response => {
        // Try to parse JSON response
        let payload = null
        try {
            payload = await response.json();
        } catch (e) {
            // not JSON
        }

        if (!response.ok) {
            // Show backend-provided error if present, otherwise status text
            const errText = payload && payload.detail ? payload.detail : (payload && payload.message ? payload.message : (response.statusText || `Error ${response.status}`));
            output.innerText = `Upload failed: ${errText}`;
            console.error('Upload failed', response.status, payload);
            return;
        }

        const data = payload || {};
        if (data.text && data.text.length > 0) {
            output.innerText = data.text;
        } else {
            output.innerText = data.message || "No text extracted";
        }
    })
    .catch(error => {
        output.innerText = "Error uploading PDF: network or client error";
        console.error(error);
    });
}
