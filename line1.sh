#!/bin/bash
# 変数の宣言：(変数名)=(変数の値)　※余計な空白文字は挿入しないこと!!
dir_name=$1
commit_hash=$2
file1=$3
destination=$4
project_name=$5
# cd コマンドを使って，git リポジトリに移動する
cd $project_name
# git コマンドを使って，file1 を復元する
git checkout ${commit_hash}^ -- $file1
# git コマンドを使って，file1 を昔のバージョンに戻す
#git checkout $commit_hash $file1
# cp コマンドを使って，file1 をdestinationにコピーする
cp $file1 $destination
# cd コマンドを使って，一つ上のディレクトリに戻る