Порядок запуска:

- рабочая директория /kubernetes-networks
запустить все файлы кроме ingress2.yaml

$ kubectl -n homework get pod
NAME                         READY   STATUS    RESTARTS   AGE
practice2-84c75c4556-kd9kw   1/1     Running   0          12m
practice2-84c75c4556-q9bzp   1/1     Running   0          12m
practice2-84c75c4556-rjpx8   1/1     Running   0          12m

$ kubectl get deploy -n homework
NAME        READY   UP-TO-DATE   AVAILABLE   AGE
practice2   3/3     3            3           81s

$ kubectl -n homework get ingress
NAME             CLASS   HOSTS           ADDRESS        PORTS   AGE
ingress-nginx1   nginx   homework.otus   192.168.49.2   80      8m10s

Проверка задачи со *
$ kubernetes -n homework delete ingress-nginx1
$ kubernetes -n homework apply -f ingress2.yaml

curl --resolve "homework.otus:80:$( minikube ip )" -i http://homework.otus

HTTP/1.1 200 OK
Date: Thu, 16 May 2024 14:24:50 GMT
Content-Type: text/plain
Content-Length: 16
Connection: keep-alive

Rewrite is work!