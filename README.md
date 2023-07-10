# intel_ai_project

# Squat Counter

* (간략히 전체 프로젝트를 설명하고, 최종 목표가 무엇인지에 대해 기술)

* real-time vedio를 송출하고 사용자가 스쿼트 동작을 수행했을 때 숫자를 counting해주고,
* 사용자의 자세에 집중할 수 있도록 background image를 제거해주는 프로그램

## Requirement

* (프로젝트를 실행시키기 위한 최소 requirement들에 대해 기술)

```
* 10th generation Intel® CoreTM processor onwards
* At least 32GB RAM
* Python 3.9
```

## Clone code

* (Code clone 방법에 대해서 기술)
  
```shell
git clone https://github.com/Jeong32/intel_ai_project/d
```

## Prerequite

* (프로잭트를 실행하기 위해 필요한 dependencies 및 configuration들이 있다면, 설치 및 설정방법에 대해 기술)

```shell
python -m venv .venv
source .venv/bin/activate

python -m pip install -U pip
python -m pip install wheel

python -m pip install openvino-dev

cd /path/to/repo/xxx/
python -m pip install -r requirements.txt
```

## Steps to build

* (프로젝트를 실행을 위해 빌드 절차 기술)

```shell
cd ~/xxxx
source .venv/bin/activate

make
make install
```

## Steps to run

* (프로젝트 실행방법에 대해서 기술, 특별한 사용방법이 있다면 같이 기술)

```shell
cd ~/xxxx
source .venv/bin/activate

cd /path/to/repo/xxx/
python demo.py -i xxx -m yyy -d zzz
```

## Output

![./images/result.jpg](./images/result.jpg)

## Appendix

* (참고 자료 및 알아두어야할 사항들 기술)
