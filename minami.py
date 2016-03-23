# -*- coding: utf-8 -*-
import os
import subprocess
import sys

f = open('minami.csv', 'r')
line = f.readline()
line = line.replace('\r', '')
line = line.replace('\n', '')
while line:
    factor = line.split(',')
    setID = factor[0]
    commit_hash = factor[1]
    file1 = factor[2]
    file2 = factor[3]
    # minami script starts here
    if file2 == "hogehoge":
        try:
            os.rmdir(setID)
        except OSError:
            file1 = file1
        os.mkdir(setID)
        # file1 を前のバージョンにもどして, setID ディレクトリにコピーする
        file_name_current = file1.split('/')[-1]
        destination =  '../' + setID  + '/' + file_name_current.split('.')[0] + '_old.csv'
        project_name = file1.split('/')[0]
        file1 = '/'.join(file1.split('/')[1:])
        argument_list = [setID, commit_hash, file1, destination, project_name]
        subprocess.call('./line1.sh ' + ' '.join(argument_list), shell = True)

    elif file1 == "hogehoge":
        # 上の処理を参考にして自分で書いてください
        file_name_current1 = file2.split('/')[-1]
        destination =  '../' + setID  + '/' + file_name_current1.split('.')[0] + '_old.csv'
        project_name = file2.split('/')[0]
        file2 = '/'.join(file2.split('/')[1:])
        argument_list = [setID, commit_hash, file2, destination, project_name]
        subprocess.call('./line2.sh ' + ' '.join(argument_list), shell = True)

    else:
        # 上の処理を参考にして自分で書いてください
        file_name_current = file1.split('/')[-1]
        destination =  '../' + setID  + '/' + file_name_current.split('.')[0] + '_new.csv'
        project_name = file1.split('/')[0]
        file1 = '/'.join(file1.split('/')[1:])
        argument_list = [setID, commit_hash, file1, destination, project_name]
        subprocess.call('./line1.sh ' + ' '.join(argument_list), shell = True)

        file_name_current1 = file2.split('/')[-1]
        destination =  '../' + setID  + '/' + file_name_current1.split('.')[0] + '_new.csv'
        project_name = file2.split('/')[0]
        file2 = '/'.join(file2.split('/')[1:])
        argument_list = [setID, commit_hash, file2, destination, project_name]
        subprocess.call('./line2.sh ' + ' '.join(argument_list), shell = True)

    line = f.readline()
    line = line.replace('\r', '')
    line = line.replace('\n', '')

"""
cp コマンドの使い方
cp (file_name) (destination)

アルゴリズムの作成
1..一行目を読み込む
3.IDの番号を取り出す
4.IDの番号を名前としたディレクトリを作成する
5.file1のfoo.javaをcommit hash1に戻す git checkout    hash値
6.cp foo.java ディレクトリへ
7.二行目を読み込む
8.var.javaを前のバージョンに戻す
9.va.javaをディレクトリにコピー
10.３行目を読み込む
11.foo.javaのバージョンを戻してコピーする
12.var.javaのバージョンを戻してコピーする
1回のループ　＝　1つの行に対する処理
"""






    #os.system('command here')
    #result = suprocess.check_output('command here', shell=True)
    # minami script ends here
