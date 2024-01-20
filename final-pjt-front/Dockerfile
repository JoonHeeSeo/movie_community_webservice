# 기본 이미지로 node의 특정 버전을 사용합니다. 여기서는 14버전을 사용하겠습니다.
FROM node:14

# 애플리케이션 코드를 포함할 작업 디렉토리를 만듭니다.
WORKDIR /app

# package.json과 package-lock.json(이 있을 경우)를 작업 디렉토리로 복사합니다.
COPY package*.json ./

# 프로젝트 의존성을 설치합니다.
RUN npm install

# 나머지 프로젝트 파일을 작업 디렉토리로 복사합니다.
COPY . .

# 프로덕션을 위한 애플리케이션을 빌드합니다.
RUN npm run build

# 애플리케이션을 실행하기 위해 컨테이너가 리스닝할 포트를 지정합니다.
EXPOSE 8080

# vue-cli-service를 이용해 서버를 구동합니다.
CMD ["npm", "run", "serve"]
