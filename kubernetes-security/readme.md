Порядок запуска:

- рабочая директория /kubernetes-security
запустить все файлы

$ kubectl get pod
NAME                         READY   STATUS    RESTARTS   AGE
practice2-84c75c4556-kd9kw   1/1     Running   0          12m
practice2-84c75c4556-q9bzp   1/1     Running   0          12m
practice2-84c75c4556-rjpx8   1/1     Running   0          12m

$ kubectl get sa
NAME      SECRETS   AGE
cd        0         5h13m
default   0         4d14h
monitor   0         64m

$ kubectl get clusterrole |grep monitor
monitor                                                                2024-05-26T20:20:14Z
system:monitoring                                                      2024-05-07T07:16:29Z

$ kubectl get clusterrolebinding |grep monitor
monitor                                                         ClusterRole/monitor
monitoring                                                      ClusterRole/system:monitoring
system:monitoring                                               ClusterRole/system:monitoring

$ kubectl get role
NAME     CREATED AT
hw_adm   2024-05-26T18:28:08Z

$ kubectl get rolebinding
NAME   ROLE          AGE
cd     Role/hw_adm   3h25m

$ kubectl exec -it practice2-69c978677f-... -- bash
curl --cacert ${CACERT} --header "Authorization: Bearer $(cat "${SA}/token")" -X  GET ${KUBEAPI}/metrics

`# TYPE aggregator_discovery_aggregation_count_total counter
aggregator_discovery_aggregation_count_total 2
`# HELP aggregator_unavailable_apiservice [ALPHA] Gauge of APIServices which are marked as unavailable broken down by APIService name.
`# TYPE aggregator_unavailable_apiservice gauge
aggregator_unavailable_apiservice{name="v1."} 0
aggregator_unavailable_apiservice{name="v1.admissionregistration.k8s.io"} 0
aggregator_unavailable_apiservice{name="v1.apiextensions.k8s.io"} 0
aggregator_unavailable_apiservice{name="v1.apps"} 0
aggregator_unavailable_apiservice{name="v1.authentication.k8s.io"} 0
aggregator_unavailable_apiservice{name="v1.authorization.k8s.io"} 0
aggregator_unavailable_apiservice{name="v1.autoscaling"} 0
aggregator_unavailable_apiservice{name="v1.batch"} 0
aggregator_unavailable_apiservice{name="v1.certificates.k8s.io"} 0
aggregator_unavailable_apiservice{name="v1.coordination.k8s.io"} 0
aggregator_unavailable_apiservice{name="v1.discovery.k8s.io"} 0


Создание kubeconfig для service account cd
$ kubectl create token cd --duration 1440m > token
$ kubectl config set-credentials cd --token=$(cat /home/ivan/isvolkoff_repo/kubernetes-security/token)
$ kubectl config set-context cd --cluster=minikube --user=cd


Проверка задания со *

$ curl --resolve "homework.otus:80:$( minikube ip )" -i http://homework.otus/metrics.html

HTTP/1.1 200 OK
Date: Sun, 26 May 2024 22:01:36 GMT
Content-Type: text/html
Content-Length: 3098973
Connection: keep-alive
Last-Modified: Sun, 26 May 2024 21:45:44 GMT
ETag: "6653ad88-2f495d"
Accept-Ranges: bytes

`# HELP aggregator_discovery_aggregation_count_total [ALPHA] Counter of number of times discovery was aggregated
`# TYPE aggregator_discovery_aggregation_count_total counter
aggregator_discovery_aggregation_count_total 2
`# HELP aggregator_unavailable_apiservice [ALPHA] Gauge of APIServices which are marked as unavailable broken down by APIService name.
`# TYPE aggregator_unavailable_apiservice gauge
aggregator_unavailable_apiservice{name="v1."} 0
aggregator_unavailable_apiservice{name="v1.admissionregistration.k8s.io"} 0
aggregator_unavailable_apiservice{name="v1.apiextensions.k8s.io"} 0
aggregator_unavailable_apiservice{name="v1.apps"} 0
aggregator_unavailable_apiservice{name="v1.authentication.k8s.io"} 0
aggregator_unavailable_apiservice{name="v1.authorization.k8s.io"} 0
aggregator_unavailable_apiservice{name="v1.autoscaling"} 0
aggregator_unavailable_apiservice{name="v1.batch"} 0
