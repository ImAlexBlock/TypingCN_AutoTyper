import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from pynput.keyboard import Controller, Key
from os import system


system("title 彳ㄐㄐ")

print("AutoTyper For Typing-CN")
print("Made By AlexBlock")

delay = int(input("设置延迟时间/秒："))

wd = webdriver.Chrome()
wd.set_window_size(800, 800)
# 等待时间
wd.implicitly_wait(20)

print("打开网页ing")
wd.get('https://barneyzhao.gitee.io/typing-cn/#/monkey')

words_box = wd.find_element(By.CLASS_NAME, "words-box")
words = words_box.find_elements(By.CLASS_NAME, "word")

text = []
for word in words:
    # 获取 word 元素下的 letter 的文本内容
    letters = word.find_elements(By.CLASS_NAME, "letter")
    word_text = ''.join([letter.text for letter in letters])
    # print(word_text)
    text.append(word_text)
print("输入内容已载入：", text)

a = 0

for i in range(30):
    KeyBoard = Controller()
    KeyBoard.type(text[a])
    KeyBoard.press(Key.space)
    time.sleep(delay + 0.01)
    KeyBoard.release(Key.space)
    a = a + 1

input("输入任意内容结束：")