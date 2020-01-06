from setuptools import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# long_description(後述)に、GitHub用のREADME.mdを指定
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='activelog', # パッケージ名(プロジェクト名)
    packages=['activelog'], # パッケージ内(プロジェクト内)のパッケージ名をリスト形式で指定

    version='1.0', # バージョン

    license='MIT', # ライセンス

    author='Tatsuya Abe', # パッケージ作者の名前
    author_email='abe12@mccc.jp', # パッケージ作者の連絡先メールアドレス

    url='https://github.com/shonansurvivors/yourpackage', # パッケージに関連するサイトのURL(GitHubなど)

    desription='To translate Japanese sentences into Son Goku accent.', # パッケージの簡単な説明
    long_description=long_description, # PyPIに'Project description'として表示されるパッケージの説明文
    long_description_content_type='text/markdown', # long_descriptionの形式を'text/plain', 'text/x-rst', 'text/markdown'のいずれかから指定
    keywords='log logger logging', # PyPIでの検索用キーワードをスペース区切りで指定

    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
    ], # パッケージ(プロジェクト)の分類。https://pypi.org/classifiers/に掲載されているものを指定可能。
)
