import random

# 파일 개수 설정
N = 3  # 파일의 개수

for i in range(N):
    # 데이터 생성 및 랜덤 섞기
    data = list(range(1000))
    random.shuffle(data)

    # CSV 파일로 저장
    output_file = f'random_solution_{i+1}.csv'
    with open(output_file, 'w') as f:
        for number in data:
            f.write(f"{number}\n")

    print(f"Random numbers saved to {output_file}")