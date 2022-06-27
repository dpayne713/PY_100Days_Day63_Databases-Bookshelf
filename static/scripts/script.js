function openModal() {
    document.getElementById("backdrop").style.display = "block"
    document.getElementById("myModal").style.display = "block"
    document.getElementById("myModal").classList.add("show")
}
function closeModal() {
    document.getElementById("backdrop").style.display = "none"
    document.getElementById("myModal").style.display = "none"
    document.getElementById("myModal").classList.remove("show")
}
// Get the modal
var modal = document.getElementById('myModal');
let open_btns = document.getElementsByClassName('openBtn')
var modalContent = document.getElementById('modal-content')

for (var i=0 ; i < open_btns.length; i++) {

    open_btns[i].addEventListener('click', function (e) {
        e.preventDefault()
        id = e.target.parentNode.dataset.id
        fetch('/update/'+ id)

            .then(function (response) {
                switch (response.status) {
                    // status "OK"
                    case 200:
                        return response.text();
                    // status "Not Found"
                    case 404:
                        throw response;
                }
            })
            .then(function (template) {
                modalContent.innerHTML = template;
                openModal()

            })
            .catch(function (response) {
                // "Not Found"
                console.log(response.statusText);
            });
        // get html from update route TODO
        // push to modal body TODO
        // turn on modal

    })

}


// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target === modal) {
      closeModal()
  }
  if (event.target.classList.contains('close')) {
      closeModal()
  }
    }