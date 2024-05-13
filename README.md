# Репозиторий для выполнения домашних заданий курса "Инфраструктурная платформа на основе Kubernetes-2024-02" 

Порядок запуска:

- рабочая директория /kubernetes-controllers
- подготовка неймспейса
`kubectl apply -f namespace.yaml`
- подготовка configmap
`kubectl apply -f configmap.yaml`
- добавляем лейбл на ноду
`kubectl label nodes minikube homework=true`
- запуск deployment
`kubectl apply -f deployment.yaml`

- проверяем что поды запустились и прошли проверку
```
$ kubectl -n homework get pod

NAME                         READY   STATUS    RESTARTS   AGE
practice2-84c75c4556-kd9kw   1/1     Running   0          12m
practice2-84c75c4556-q9bzp   1/1     Running   0          12m
practice2-84c75c4556-rjpx8   1/1     Running   0          12m
```
