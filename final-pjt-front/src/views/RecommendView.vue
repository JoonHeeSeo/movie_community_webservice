<template>
  <div>
    <!-- 등록되는 단어 확인 -->
    <div style="display: flex; justify-content: center; align-items: center; height: 60px;">
      <div class="word-show-container">{{ resultword }}</div>
    </div>

    <!-- 등록된 단어 확인하기 -->
    <div style="display: flex; justify-content: center; align-items: center; height: 60px; margin-top:10px;">
      <span class="word-select-container">{{ result1 }}</span>
      <span class="word-select-container">{{ result2 }}</span>
      <span class="word-select-container">{{ result3 }}</span>
    </div>
    
    <!-- 단어 선택 버튼  -->
    <form>
      <div style="display: flex; justify-content: center;">
        <input type="submit" value="단어등록" @click.prevent="makeWord()" style="background: none; color:white; border:solid white 1px; padding:10px; cursor:pointer; margin:10px;">
        <input type="submit" value="추천" @click.prevent="sendWord()" style="background: none; color:white; border:solid white 1px; padding:10px; cursor:pointer; margin:10px;">
        <input type="submit" value="새로고침" @click="resetGame()" style="background: none; color:white; border:solid white 1px; padding:10px; cursor:pointer; margin:10px;">
      </div>
    </form>
    
    <hr style="border: solid #fff 1px;">

    <!-- 추천영화 -->
    <!-- <div style="display: flex; justify-content: center; align-items: center; flex-direction: column; height: 10vh;">
      <p style="background: none; color: white; margin-bottom: 5px; font-size: 26px;"></p>
    </div> -->
    <p style="display: flex; justify-content: center; align-items: center;">
      <router-link v-for="movie in movies" :key="movie.id" :to="{ name: 'moviedetail/:movie_id', params: { movie_id: movie.id } }">
        <img :src="getMoviePoster(movie.poster_path)" alt="movie_post" style="margin-right: 30px;">
      </router-link>
    </p>

    <!-- 빙고 판 -->
    <div class="bingo-container">
      <table id="tblBingo"></table>
    </div>
    <br>

    


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
      arr: [],

      resultIdx: 1,
      result1: '',
      result2: '',
      result3: '',
      resultword: '',
      resultwordlist: [],
      movies: [],

      latestiPosition: 0,
      latestjPosition: 0,
      // 0은 초기값 1상 2하 3좌 4우
      latestDirection: 0,

    };
  },

  mounted() {
    this.table = document.querySelector("#tblBingo")
    this.letter = document.querySelectorAll(".letters-bingo")

    // this.arr = [
    //   '해', '반', '지', '기', '생', '공', '포', '니',
    //   '리', '지', '대', '봄', '가', '바', '모', '누',
    //   '스', '법', '숲', '치', '이', '보', '놀', '나',
    //   '릴', '포', '바', '리', '피', '의', '저', '도',
    //   '러', '츠', '름', '고', '오', '너', '섬', '지',
    //   '로', '삶', '여', '보', '문', '나', '건', '마',
    //   '맨', '겨', '울', '바', '고', '어', '른', '그',
    //   '스', '연', '애', '재', '강', '아', '일', '리',
    // ]

    // this.arr = [
    //   '대', '왕', '지', '반', '해', '울', '가', '에',
    //   '부', '주', '간', '자', '리', '겨', '을', '즈',
    //   '탈', '공', '맨', '크', '제', '름', '봄', '트',
    //   '출', '드', '용', '다', '성', '여', '그', '스',
    //   '마', '필', '기', '름', '반', '씨', '린', '바',
    //   '리', '주', '행', '이', '인', '날', '북', '마',
    //   '오', '질', '방', '람', '양', '기', '자', '도',
    //   '분', '노', '명', '사', '침', '탑', '전', '거',
    // ]

    this.arr = [
      '사', '슴', '마', '리', '오', '문', '컴', '아',
      '브', '가', '디', '언', '즈', '단', '포', '기',
      '라', '오', '브', '슈', '퍼', '속', '넌', '공',
      '더', '갤', '럭', '시', '수', '헌', '트', '룡',
      '스', '필', '기', '름', '드', '래', '곤', '둘',
      '분', '노', '의', '질', '주', '라', '메', '리',
      '존', '인', '공', '렌', '필', '드', '간', '마',
      '윅', '어', '주', '이', '블', '즈', '짱', '구',
    ]
    

    // this.shuffle(this.arr)
    this.initializeBingoTable()
  },

  methods: {
    initializeBingoTable() {
      let iterator = 0

      for (let i = 0; i < 8; i++) {
        let tr = document.createElement("tr")
        this.table.appendChild(tr)

        for (let j = 0; j < 8; j++) {
          let td = document.createElement("td")
          // td.textContent = this.arr[iterator].toString()
          // td.style.height = "20%"
          td.style.width = "50px"
          td.classList.add("main-table-cell")

          let div = document.createElement("div")
          div.classList.add("cell-format")
          div.id = this.arr[iterator]+ ',' + (i + 1) + ',' + (j + 1)
          div.textContent = this.arr[iterator].toString()
          td.appendChild(div)
          tr.appendChild(td)
          iterator++
        }
      }

      const cell = document.querySelectorAll(".main-table-cell")
      cell.forEach((e) => {
        e.addEventListener("click", () => {

          const divElement = e.querySelector('div')
          const newChar = divElement.id[0]
          const newiPosition = divElement.id[2]
          const newjPosition = divElement.id[4]

          // 첫번째 낱말 클릭
          if (this.latestiPosition === 0 && this.latestjPosition === 0) {          
            this.resultwordlist.push(newChar)
            this.resultword = this.resultwordlist.join("")
            e.classList.add("strickout")
            this.latestiPosition = newiPosition
            this.latestjPosition = newjPosition
          }

          else if ((Math.abs(this.latestiPosition - newiPosition) + Math.abs(this.latestjPosition - newjPosition)) === 1) {
            if ((this.latestDirection === 0) ||
                (this.latestiPosition - newiPosition === 1 && this.latestDirection === 2) ||
                (this.latestiPosition - newiPosition === -1 && this.latestDirection === 1) ||
                (this.latestjPosition - newjPosition === 1 && this.latestDirection === 4) ||
                (this.latestjPosition - newjPosition === -1 && this.latestDirection === 3)) {

            this.resultwordlist.push(newChar)
            this.resultword = this.resultwordlist.join("")
            e.classList.add("strickout")
            
            // 마지막 방향 기록
            if (this.latestiPosition - newiPosition === 1) {
              this.latestDirection = 2
            } else if (this.latestiPosition - newiPosition === -1) {
              this.latestDirection = 1
            } else if (this.latestjPosition - newjPosition === 1) {
              this.latestDirection = 4
            } else if (this.latestjPosition - newjPosition === -1) {
              this.latestDirection = 3
            }
            
            // 마지막 좌표 기록
            this.latestiPosition = newiPosition
            this.latestjPosition = newjPosition
            }
          }
        })
      })
    },

    // shuffle(arr) {
    //   let currentIndex = arr.length,
    //     randomIndex

    //   while (currentIndex != 0) {
    //     randomIndex = Math.floor(Math.random() * currentIndex)
    //     currentIndex--
    //     [arr[currentIndex], arr[randomIndex]] = [arr[randomIndex], arr[currentIndex]]
    //   }
    //   return arr
    // },

    resetGame() {
      this.latestiPoistion = 0
      this.latestjPosition = 0
    },

    sendWord() {
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
            alert("추천 영화가 생성되었습니다.")
          })
          .catch((err) => {
            console.log(err)
          })
    },

    makeWord() {
      if (this.resultIdx < 4 &&  this.resultwordlist.length === 0) {
        // resultwordlist is empty
        alert('입력값이 없습니다.')
      } else if (this.resultIdx === 1) {
        this.result1 = this.resultwordlist.join('')
        this.resultword = ''
        this.resultwordlist = []
        this.latestiPosition = 0
        this.latestjPosition = 0
        this.latestDirection = 0
        this.resultIdx = 2
      } else if (this.resultIdx === 2) {
        this.result2 = this.resultwordlist.join('')
        this.resultword = ''
        this.resultwordlist = []
        this.latestiPosition = 0
        this.latestjPosition = 0
        this.latestDirection = 0
        this.resultIdx = 3
      } else if (this.resultIdx === 3) {
        this.result3 = this.resultwordlist.join('')
        this.resultword = ''
        this.resultwordlist = []
        this.latestiPosition = 0
        this.latestjPosition = 0
        this.latestDirection = 0
        this.resultIdx = 4
      } else if (this.resultIdx === 4) {
        this.sendWord()
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
    /* width: 60%; */
    height: 40rem;
    width: 40rem;
    text-align: center;
    font-size: 26pt;
    cursor: pointer;
    margin-top:20px;
}

#tblBingo td {
    padding: 5px;
    /* flex: 1; */
    width: 20%;
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


.word-show-container{
  background: none;
  color:white;
  border:solid white 1px;
  font-size: 25px;
  width:auto;
  padding: 10px;
}
.word-select-container{
  background: rgb(244, 232, 242);
  border: solid black 1px;
  color: black;
  margin: 0px 10px 5px 10px;
  font-size: 25px;
  padding: 10px
}
/* .word-show-container:empty{
  display:none;
} */
.word-show-container:empty::before{
  content:'단어를 만들어 주세요';
}
.word-select-container:empty{
  display:none;
}

/* 추천영화 */
.recommend-movie-container{
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  height: 10vh;
}
.recommend-movie-container:empty{
  height: 0;
}

</style>