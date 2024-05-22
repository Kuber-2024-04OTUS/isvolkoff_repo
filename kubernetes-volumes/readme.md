Порядок запуска:

- рабочая директория /kubernetes-networks
запустить все файлы

$ kubectl -n homework get pod
NAME                         READY   STATUS    RESTARTS   AGE
practice2-84c75c4556-kd9kw   1/1     Running   0          12m
practice2-84c75c4556-q9bzp   1/1     Running   0          12m
practice2-84c75c4556-rjpx8   1/1     Running   0          12m

$ kubectl get deploy -n homework
NAME        READY   UP-TO-DATE   AVAILABLE   AGE
practice2   3/3     3            3           81s

$ kubectl -n homework get sc
NAME                 PROVISIONER                RECLAIMPOLICY   VOLUMEBINDINGMODE   ALLOWVOLUMEEXPANSION   AGE
sc-custom            k8s.io/minikube-hostpath   Retain          Immediate           true                   2m28s
standard (default)   k8s.io/minikube-hostpath   Delete          Immediate           false                  14d

$ kubectl -n homework get pvc
NAME      STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS   VOLUMEATTRIBUTESCLASS   AGE
hw-conf   Bound    pvc-716dcc4b-a759-417d-94b0-184ca7534cc8   1Gi        RWO            sc-custom      <unset>                 2m10s

$ curl --resolve "homework.otus:80:$( minikube ip )" -i http://homework.otus/conf/file

HTTP/1.1 200 OK
Date: Wed, 22 May 2024 06:59:13 GMT
Content-Type: text/plain
Content-Length: 39
Connection: keep-alive
Last-Modified: Wed, 22 May 2024 06:58:22 GMT
ETag: "664d978e-27"
Accept-Ranges: bytes

host: homework.otus
DEBUG: "false"