# git 02

## 혼자 작업시 conflict 해결하기

2개 이상의 컴퓨터에서 같은 원격 저장소 사용시

1. $ git add .

2. $ git commit -m '메세지'

3. $ git push origin master

   1. 잘 된다 => GOOD

   2. 안된다 

      ```
      hint: Updates were "rejected" because the tip of your
      current branch is behind
      hint: its remote counterpart. Integrate the remote changes (e.g.
      hint: '"git pull" ...') before pushing again.
      hint: See the 'Note about fast-fowards' in 'git
      push --help' for details.
      ```

4. $ git pull origin master

   1. 자동 병합(auto merge)이 일어난다.

      - $ git status 에 아무런 알림이 없다.

   2. 자동 병합에 실패 => 5번으로

      ```
      Automatic merge failed; fix conflicts and then 
      ```

      
