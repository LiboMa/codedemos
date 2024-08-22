# Deploy Argocd Application for your application

## prerequisite
kubectl
helm
argocd
github actions
docker

## Deploy

### deploy for the test environment

kubectl apply -f eks-flask-test-chart.yaml
### deploy prod environment

kubectl apply -f eks-flask-prod-chart.yaml
