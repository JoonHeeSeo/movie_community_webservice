<template>
  <div>
    <h1>algo</h1>
    <div class="bingo-container">
        <table id="tblBingo"></table>
    </div>
    <div class="letter-div">
        <table id="tblLetter">
            <tr>
                <td class="letters-bingo">B</td>
                <td class="letters-bingo">I</td>
                <td class="letters-bingo">N</td>
                <td class="letters-bingo">G</td>
                <td class="letters-bingo">O</td>
            </tr>
        </table>
    </div>
  </div>
</template>

<script>
export default {
  name:'RecommendView',  data() {
    return {
      table: null,
      letter: null,
      winningPositions: [
        [0, 1, 2, 3, 4],
        [5, 6, 7, 8, 9],
        [10, 11, 12, 13, 14],
        [15, 16, 17, 18, 19],
        [20, 21, 22, 23, 24],
        [0, 5, 10, 15, 20],
        [1, 6, 11, 16, 21],
        [2, 7, 12, 17, 22],
        [3, 8, 13, 18, 23],
        [4, 9, 14, 19, 24]
      ],
      arr: []
    };
  },
  mounted() {
    this.table = document.querySelector("#tblBingo");
    this.letter = document.querySelectorAll(".letters-bingo");
    this.arr = Array.apply(null, { length: 26 }).map(Number.call, Number);
    this.arr.shift();
    this.shuffle(this.arr);
    this.initializeBingoTable();
  },
  methods: {
    initializeBingoTable() {
      let iterator = 0;

      for (let i = 0; i < 5; i++) {
        let tr = document.createElement("tr");
        this.table.appendChild(tr);

        for (let j = 0; j < 5; j++) {
          let td = document.createElement("td");
          td.id = this.arr[iterator].toString();
          td.style.height = "20%";
          td.style.width = "20%";
          td.classList.add("main-table-cell");

          let div = document.createElement("div");
          div.classList.add("cell-format");
          div.textContent = this.arr[iterator].toString();
          td.appendChild(div);
          tr.appendChild(td);
          iterator++;
        }
      }

      const cell = document.querySelectorAll(".main-table-cell");
      let winningIterator = 0;
      cell.forEach((e) => {
        e.addEventListener("click", () => {
          e.classList.add("strickout");

          if (this.matchWin()) {
            this.letter[winningIterator].classList.add("show-bingo");

            winningIterator++;
            if (winningIterator === 5) {
              alert("B I N G O");
              this.resetGame();
            }
          }
        });
      });
    },
    shuffle(arr) {
      let currentIndex = arr.length,
        randomIndex;

      while (currentIndex != 0) {
        randomIndex = Math.floor(Math.random() * currentIndex);
        currentIndex--;

        [arr[currentIndex], arr[randomIndex]] = [
          arr[randomIndex],
          arr[currentIndex]
        ];
      }

      return arr;
    },
    matchWin() {
      const cell = document.querySelectorAll(".main-table-cell");

      return this.winningPositions.some((combination) => {
        let ite = 0;
        combination.forEach((index) => {
          if (cell[index].classList.contains("strickout")) ite++;
        });

        if (ite === 5) {
          let indexWin = this.winningPositions.indexOf(combination);
          this.winningPositions.splice(indexWin, 1);
        }

        return combination.every((index) => {
          return cell[index].classList.contains("strickout");
        });
      });
    },
    resetGame() {
      // Reset the game state here
      // This method should clear the marked cells and reinitialize the table
      // You can reset the necessary data properties or call another method to handle the reset logic
    }
  },
  computed: {
    // Define a computed property to access and display the 'arr' array
    displayedArr() {
      return this.arr.join(", ");
    }
  }
}
</script>

<style>

bingo-body {
    margin: 0;
    padding: 0;
    padding-top: 30px;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

bingo-body:focus {
    outline: none;
}

.bingo-container {
    width: 100vw;
    display: flex;
    justify-content: center;
}

#tblBingo {
    border-collapse: collapse;
    height: 25rem;
    width: 25rem;
    text-align: center;
    font-size: 22pt;
    cursor: pointer;
}

#tblBingo td {
    padding: 0.3rem;
 }

 .cell-format {
    height: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    border-radius: 20%;
    border: 0.5px solid #cccece;
}

.cell-format:hover {
    background-color: #cccece;
}

.letter-div {
    height: 20vh;
    display: flex;
    justify-content: center;
    align-items: center;
}

.letters-bingo {
    padding: 0 1.3rem;
    font-size: 40pt;
    display: none;
}

.strickout {
    text-decoration: line-through;
    color: #a6a3a3;
    font-size: 18pt;
    pointer-events: none;
}

.show-bingo {
    display: inline;
}

</style>