finalTagId = document.querySelector("#tag_id")
tagInputs = document.querySelectorAll(".tag-input")

selectedIndex = -1
finalTagId.value = -1

tagInputs.forEach((element, index) => {
    element.addEventListener("click", event => {
        event.preventDefault()
        if (element.classList.contains("tag-input--selected")) { //was selected
            tagInputs[selectedIndex].classList.remove("tag-input--selected")
            selectedIndex = -1
            finalTagId.value = -1
        } else { //was not selected
            if (selectedIndex >= 0) tagInputs[selectedIndex].classList.remove("tag-input--selected")
            selectedIndex = index
            tagInputs[selectedIndex].classList.add("tag-input--selected")
            finalTagId.value = element.value
        }
    })
})