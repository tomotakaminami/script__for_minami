#!/bin/bash
# 変数の宣言：(変数名)=(変数の値)　※余計な空白文字は挿入しないこと!!
dir_name=$1
commit_hash=$2
file2=$3
destination=$4
project_name=$5
# cd コマンドを使って，git リポジトリに移動する
cd $project_name
# git コマンドを使って，file2 を復元する
git checkout ${commit_hash}^ -- $file2
# git コマンドを使って，file2 を昔のバージョンに戻す
#git checkout $commit_hash $file2
# cp コマンドを使って，file2 をdestinationにコピーする
cp $file2 $destination
# cd コマンドを使って，一つ上のディレクトリに戻る 