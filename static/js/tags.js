tagLis = document.querySelectorAll(".tag-list__li")

tagLis.forEach((tag, index) => {
    console.log(tag)
    tag.addEventListener("click", (event) => {
        event.preventDefault()
        if(confirm(`Do you wish to delete '${tag.innerHTML}'?`)) {
            window.location.replace(`/delete_tag/${tag.value}`)
        }
    })
})
