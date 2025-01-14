let url = "http://127.0.0.1:5005/classify_flower"

form = document.getElementById("flowerForm");

form.addEventListener("submit", (e) => {
    e.preventDefault();

   formData = new FormData(e.target)
   formDataObject = Object.fromEntries(formData)
   
//    console.log(formDataObject);

fetch(url, {
    method: "POST",
    headers: {
        "Content-Type": "application/json"
    },
    body: JSON.stringify(formDataObject)
})
.then(res => res.json())
.then(data => console.log(data))
.catch(error => console.log("Error", error))
   
});