### Deploy to Argocd


#### prerequisite
kubectl
helm
argocd
github actions
docker

### Deploy

kubectl apply -f eks-flask-test-chart.yaml
kubectl apply -f eks-flask-prod-chart.yaml
