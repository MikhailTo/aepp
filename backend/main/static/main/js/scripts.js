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

function drawSquares() {
        const canvas = document.getElementById('canvas');
        const ctx = canvas.getContext('2d');

        let r = 51;
        for (let x = 40; x < 2850; x += 50) {
          ctx.moveTo(x, 450);
          ctx.lineTo(x, 480);
          ctx.fillText(r += 2, x - 4, 500)
        }
        ctx.strokeStyle = "#888";
        ctx.stroke();

        this.squares.forEach((square) => {
          ctx.fillStyle= square.color;
          ctx.strokeStyle="black";
          ctx.lineWidth=5;
          ctx.shadowColor = 'black';
          ctx.fillRect(square.x, square.y, square.w, square.h);
          ctx.font = '10px Arial';
          ctx.textAlign = 'center';
          ctx.fillBaseline = 'middle';
          ctx.fillStyle = 'white';
          ctx.fillText(square.name, square.x + square.w / 2, square.y + square.h / 2);
        });
      }

