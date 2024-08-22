# Python-flask app demo for gitops on EKS

## Links
 * [refer link](https://zhuanlan.zhihu.com/p/78432719)
 * https://yeasy.gitbooks.io/docker_practice/install/mirror.html


## Definition in Github action

### Checkout the content defined in CI Part
.github/workflows/github-actions-demo.yml

### Modify the code as needed 
Note: **we use  test envs including `chartDev`, `chartTest`, and `chartProd` which no need to modified mannually.**

1. Just simplly modify the code directly. 

* cd app/
* change app.py

2. git push and commit the code

git add -A
git commit -m "some comment `date %Y%-%T`"
git push 

3. checkout the action executions
checkout the link: https://github.com/LiboMa/codedemos/actions 

4. checkout the argocd management url, for me this time



