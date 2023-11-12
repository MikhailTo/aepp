// const container = document.getElementById("container")
const sidebar = document.getElementById("sidebar")
const openSidebar = () => {
    // sidebar.classList.toggle("sidebar--is-hidden")
    if (sidebar.style.display === "block") {
        sidebar.style.display = "none"
    } else {
        sidebar.style.display = "block"
    }
}

