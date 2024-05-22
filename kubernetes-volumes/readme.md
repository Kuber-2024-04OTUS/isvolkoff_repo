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
NAME             STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS   VOLUMEATTRIBUTESCLASS   AGE
pvc-custom-cs    Bound    pvc-70be9405-3f71-4ccc-a126-f685af1c9e51   1Gi        RWO            sc-custom      <unset>                 83s
pvc-default-cs   Bound    pvc-5acae0a2-0d2f-4352-a46d-41d29038ef04   1Gi        RWO            standard       <unset>                 90s

$ k describe deploy practice2 |grep ClaimName
ClaimName:  pvc-default-cs

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

Проверка задачи со *
заменить в deployment.yaml claimName: pvc-default-cs на pvc-custom-cs
$ kubernetes apply -f deployment.yaml

$ k describe deploy practice2 |grep ClaimName
ClaimName:  pvc-custom-cs
