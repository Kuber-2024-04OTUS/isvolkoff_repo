устанавливаем prometheus из bitnami
копируем и создаем образ из директории nginx в minikube
запускаем nginx.yaml и servicemonitor.yaml

- deploy
NAME                                           READY   UP-TO-DATE   AVAILABLE   AGE
custom-nginx                                   1/1     1            1           22m
my-release-kube-prometheus-blackbox-exporter   1/1     1            1           31m
my-release-kube-prometheus-operator            1/1     1            1           31m
my-release-kube-state-metrics                  1/1     1            1           31m

- pods
NAME                                                            READY   STATUS    RESTARTS      AGE
alertmanager-my-release-kube-prometheus-alertmanager-0          2/2     Running   0             31m
custom-nginx-756685c9bd-qlksj                                   2/2     Running   0             23m
my-release-kube-prometheus-blackbox-exporter-747b64bbf5-fwfkj   1/1     Running   0             31m
my-release-kube-prometheus-operator-68698cf48b-8ktjf            1/1     Running   0             31m
my-release-kube-state-metrics-6699cc894d-75txh                  1/1     Running   0             31m
my-release-node-exporter-6rx2t                                  1/1     Running   0             31m
network-miltitul                                                1/1     Running   2 (25h ago)   3d1h
prometheus-my-release-kube-prometheus-prometheus-0              2/2     Running   0             31m

- servicemonitor
NAME                                                 AGE
hw-nginx                                             14m
my-release-kube-prometheus-alertmanager              32m
my-release-kube-prometheus-apiserver                 32m
my-release-kube-prometheus-coredns                   32m
my-release-kube-prometheus-kube-controller-manager   32m
my-release-kube-prometheus-kube-proxy                32m
my-release-kube-prometheus-kube-scheduler            32m
my-release-kube-prometheus-kubelet                   32m
my-release-kube-prometheus-operator                  32m
my-release-kube-prometheus-prometheus                32m
my-release-kube-state-metrics                        32m
my-release-node-exporter                             32m
