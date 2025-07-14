
# anaconda(또는 miniconda)가 존재하지 않을 경우 설치해주세요!
## TODO
if ! command -v conda &> /dev/null; then
    echo "conda not found. Installing..."
    wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh
    bash miniconda.sh -b -p $HOME/miniconda
    eval "$($HOME/miniconda/bin/conda shell.bash hook)"
fi


# Conda 환셩 생성 및 활성화
## TODO
conda create -y -n myenv python=3.10

source $HOME/miniconda/bin/activate myenv

pip install mypy

## 건드리지 마세요! ##
python_env=$(python -c "import sys; print(sys.prefix)")
if [[ "$python_env" == *"/envs/myenv"* ]]; then
    echo "[INFO] 가상환경 활성화: 성공"
else
    echo "[INFO] 가상환경 활성화: 실패"
    exit 1 
fi

# 필요한 패키지 설치
## TODO

# Submission 폴더 파일 실행
cd submission || { echo "[INFO] submission 디렉토리로 이동 실패"; exit 1; }

for file in *.py; do
    ## TODO
    filename=$(basename "$file" .py)
    python "$file" < "/mnt/c/Users/user/Documents/YBIGTA_newbie_assignment/1(2)-CS_basics/input/${filename}_input" > "../output/${filename}_output"
done

# mypy 테스트 실행 및 mypy_log.txt 저장
## TODO
mypy *.py > ../mypy_log.txt



# conda.yml 파일 생성
## TODO
conda env export > ../conda.yml


# 가상환경 비활성화
## TODO
conda deactivate