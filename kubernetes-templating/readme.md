- рабочая директория /kubernetes-templating
$ helm dependency build
$ helm install hw .

NAME: hw
LAST DEPLOYED: Sun Jun  2 19:09:01 2024
NAMESPACE: default
STATUS: deployed
REVISION: 1
TEST SUITE: None
NOTES:
http://homework.otus

$ helm list
NAME    NAMESPACE       REVISION        UPDATED                                 STATUS          CHART           APP VERSION
hw      default         1               2024-06-02 19:21:06.451870394 +0300 MSK deployed        nginx-0.1.0     1.16.0
$ kubectl -n homework get pod
NAME                        READY   STATUS    RESTARTS   AGE
nginx-hw-54c4b9b56d-g4m6j   1/1     Running   0          2m
nginx-hw-54c4b9b56d-gn7lg   1/1     Running   0          2m
nginx-hw-54c4b9b56d-x5bbl   1/1     Running   0          2m

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

Проверка заданиея 2:
$ helmfile apply
$ helm list -n prod
NAME    NAMESPACE       REVISION        UPDATED                                 STATUS          CHART           APP VERSION
kafka1  prod            1               2024-06-02 16:29:14.608938902 +0000 UTC deployed        kafka-25.3.5    3.5.1
$ helm list -n dev
NAME    NAMESPACE       REVISION        UPDATED                                 STATUS          CHART           APP VERSION
kafka2  dev             1               2024-06-02 16:29:14.605793602 +0000 UTC deployed        kafka-29.2.0    3.7.0
