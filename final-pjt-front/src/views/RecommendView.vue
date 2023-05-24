<template>
  <div>

    <div class="bingo-container">
        <table id="tblBingo"></table>
    </div>
    <br>
    <!-- <div class="letter-div">
        <table id="tblLetter">
            <tr>
                <td class="letters-bingo">A</td>
                <td class="letters-bingo">I</td>
                <td class="letters-bingo">N</td>
                <td class="letters-bingo">G</td>
                <td class="letters-bingo">O</td>
            </tr>
        </table>
    </div> -->

    <form>
      <div style="display: flex; justify-content: center;">
        <input type="submit" value="NEXT" @click.prevent="makeWord()" style="background: none; color:white; border:solid white 1px; padding:10px; cursor:pointer; margin-right: 10px;">
        <input type="submit" value="초기화" @click="resetGame()" style="background: none; color:white; border:solid white 1px; padding:10px; cursor:pointer;">
      </div>
    </form>

    <div style="display: flex; justify-content: center; align-items: center; flex-direction: column; height: 10vh;">
      <div style="background: none; color: white; border: solid white 1px; padding: 10px; cursor: pointer; margin-bottom: 10px; font-size: 26px;">{{ resultword }}</div>
      <div style="margin-bottom: 5px;"></div>
    </div>

    <div style="display: flex; justify-content: center; align-items: center; flex-direction: column; height: 10vh;">
      <p style="background: none; color: white; margin-bottom: 5px; font-size: 26px;">첫번째 단어 : {{ result1 }}</p>
      <p style="background: none; color: white; margin-bottom: 5px; font-size: 26px;">두번째 단어 : {{ result2 }}</p>
      <p style="background: none; color: white; margin-bottom: 5px; font-size: 26px;">세번째 단어 : {{ result3 }}</p>
    </div>
    <br><hr>

    <div style="display: flex; justify-content: center; align-items: center; flex-direction: column; height: 10vh;">
      <p style="background: none; color: white; margin-bottom: 5px; font-size: 26px;">추천 영화</p>
    </div>

    <p style="display: flex; justify-content: center; align-items: center;">
      <router-link v-for="movie in movies" :key="movie.id" :to="{ name: 'moviedetail/:movie_id', params: { movie_id: movie.id } }">
        <img :src="getMoviePoster(movie.poster_path)" alt="movie_post" style="margin-right: 30px;">
      </router-link>
    </p>
      
    <!-- <p v-for="movie in movies" :key="movie.id">
      <router-link :to="{ name: 'moviedetail/:movie_id', params: { movie_id: movie.id } }">
      <img :src="getMoviePoster(movie.poster_path)" alt="movie_post">
      </router-link>
    </p> -->
      <!-- {{ movie.title }} -->
      <!-- <button class="ticket-detail-btn">자세히 보기</button> -->


    <!-- movie_id = models.IntegerField()
    original_title = models.TextField(null=True, blank=True)    
    title = models.TextField(null=True, blank=True)
    original_language = models.TextField(null=True, blank=True)
    genre_ids = models.TextField(null=True, blank=True)
    overview = models.TextField(null=True, blank=True)
    release_date = models.TextField(null=True, blank=True)
    popularity = models.IntegerField(null=True, blank=True)
    vote_average = models.FloatField(null=True, blank=True)
    vote_count = models.IntegerField(null=True, blank=True)
    adult = models.TextField(null=True, blank=True)
    video = models.TextField(null=True, blank=True)
    poster_path = models.TextField(null=True, blank=True)
    backdrop_path = models.TextField(null=True, blank=True) -->

  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name:'RecommendView',  data() {
    return {
      table: null,
      letter: null, 
      // winningPositions: [
      //   [0, 1, 2, 3, 4],
      //   [5, 6, 7, 8, 9],
      //   [10, 11, 12, 13, 14],
      //   [15, 16, 17, 18, 19],
      //   [20, 21, 22, 23, 24],
      //   [0, 5, 10, 15, 20],
      //   [1, 6, 11, 16, 21],
      //   [2, 7, 12, 17, 22],
      //   [3, 8, 13, 18, 23],
      //   [4, 9, 14, 19, 24]
      // ],
      arr: [],

      resultIdx: 1,
      result1: '',
      result2: '',
      result3: '',
      resultword: '',
      resultwordlist: [],
      movies: [],

    };
  },

  mounted() {
    this.table = document.querySelector("#tblBingo");
    this.letter = document.querySelectorAll(".letters-bingo");

    // this.arr = [
    //   '해', '반', '지', '기', '생', '공', '포', '니',
    //   '리', '지', '대', '봄', '가', '바', '모', '누',
    //   '스', '법', '숲', '치', '이', '보', '놀', '나',
    //   '릴', '포', '바', '리', '피', '의', '저', '도',
    //   '러', '츠', '름', '고', '오', '너', '섬', '지',
    //   '로', '삶', '여', '보', '문', '나', '건', '마',
    //   '맨', '겨', '울', '바', '고', '어', '른', '그',
    //   '스', '연', '애', '재', '강', '아', '일', '리',
    // ];


    this.arr = [
      '대', '왕', '지', '반', '해', '울', '가', '에',
      '부', '주', '간', '자', '리', '겨', '을', '즈',
      '탈', '공', '맨', '크', '제', '름', '봄', '트',
      '출', '드', '용', '다', '성', '여', '그', '스',
      '마', '필', '기', '름', '반', '씨', '린', '바',
      '리', '주', '행', '이', '인', '날', '북', '마',
      '오', '질', '방', '람', '양', '기', '자', '도',
      '분', '노', '명', '사', '침', '탑', '전', '거',
    ];


    console.log(this.arr)
    

    this.shuffle(this.arr);
    this.initializeBingoTable();
  },

  methods: {
    initializeBingoTable() {
      let iterator = 0;

      for (let i = 0; i < 8; i++) {
        let tr = document.createElement("tr");
        this.table.appendChild(tr);

        for (let j = 0; j < 8; j++) {
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
      // let winningIterator = 0;
      cell.forEach((e) => {
        e.addEventListener("click", () => {
          
          
          // test part -start

          console.log(e.id)
          this.resultwordlist.push(e.id)
          this.resultword = this.resultwordlist.join("")
          console.log(this.resultwordlist)

          // test part -end



          e.classList.add("strickout");
          // e.classList.toggle("strickout");



          // if (this.matchWin()) {
          //   this.letter[winningIterator].classList.add("show-bingo");

          //   winningIterator++;
          //   if (winningIterator === 5) {
          //     alert("B I N G O");
          //     this.resetGame();
          //   }
          // }



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

    // matchWin() {
    //   const cell = document.querySelectorAll(".main-table-cell");

    //   return this.winningPositions.some((combination) => {
    //     let ite = 0;
    //     combination.forEach((index) => {
    //       if (cell[index].classList.contains("strickout")) ite++;
    //     });

    //     if (ite === 5) {
    //       let indexWin = this.winningPositions.indexOf(combination);
    //       this.winningPositions.splice(indexWin, 1);
    //     }

    //     return combination.every((index) => {
    //       return cell[index].classList.contains("strickout");
    //     });
    //   });
    // },

    resetGame() {
      // This method should clear the marked cells and reinitialize the table
    },

    makeWord() {
      if (this.resultIdx < 4 &&  this.resultwordlist.length === 0) {
        // resultwordlist is empty
        alert('입력값이 없습니다.')
      } else if (this.resultIdx === 1) {
        this.result1 = this.resultwordlist.join('')
        this.resultword = ''
        this.resultwordlist = []
        this.resultIdx = 2
      } else if (this.resultIdx === 2) {
        this.result2 = this.resultwordlist.join('')
        this.resultword = ''
        this.resultwordlist = []
        this.resultIdx = 3
      } else if (this.resultIdx === 3) {
        this.result3 = this.resultwordlist.join('')
        this.resultword = ''
        this.resultwordlist = []
        this.resultIdx = 4
      } else if (this.resultIdx === 4) {
        const resultInput = []
        resultInput.push(this.result1)
        resultInput.push(this.result2)
        resultInput.push(this.result3)

        axios({
          method: 'post',
          url: `${API_URL}/movies/recommend/`,
          data: { resultInput },
          headers: {
            Authorization: `Token ${this.$store.state.token}`
          },
        })
          .then((res) => {
            this.movies = res.data
            console.log(res)
          })
          .catch((err) => {
            console.log(err)
          })
      }
    },


    getMoviePoster(poster_path) {
      if(poster_path) {
        return "https://image.tmdb.org/t/p/w200" + poster_path
      } else {
        return "https://upload.wikimedia.org/wikipedia/commons/1/14/No_Image_Available.jpg?20200913095930"
      }
    },
    
  },
  




  // computed: {
  //   // Define a computed property to access and display the 'arr' array
  //   displayedArr() {
  //     return this.arr.join(", ");
  //   }
  // }


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
    width: 40%;
    /* height: 40rem; */
    /* width: 40rem; */
    text-align: center;
    font-size: 26pt;
    cursor: pointer;
}

#tblBingo td {
    padding: 0.5rem;
    flex: 1;
    /* width: 20%; */
 }

 .cell-format {
    height: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    border-radius: 20%;
    border: 1px solid #cccece;
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
    padding: 0 1.5rem;
    font-size: 48pt;
    display: none;
}

.strickout {
    text-decoration: line-through;
    color: #a6a3a3;
    font-size: 24pt;
    pointer-events: none;
}

.show-bingo {
    display: inline;
}

</style>