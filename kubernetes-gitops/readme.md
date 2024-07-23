NAME                        STATUS   ROLES    AGE     VERSION   INTERNAL-IP   EXTERNAL-IP   OS-IMAGE             KERNEL-VERSION      CONTAINER-RUNTIME     LABELS
cl19jdq4f34mf9f213r5-ukew   Ready    <none>   10m     v1.26.2   10.129.0.36   <none>        Ubuntu 20.04.6 LTS   5.4.0-177-generic   containerd://1.6.28   beta.kubernetes.io/arch=amd64,beta.kubernetes.io/instance-type=standard-v3,beta.kubernetes.io/os=linux,failure-domain.beta.kubernetes.io/zone=ru-central1-b,kubernetes.io/arch=amd64,kubernetes.io/hostname=cl19jdq4f34mf9f213r5-ukew,kubernetes.io/os=linux,node-group-name=infra,node.kubernetes.io/instance-type=standard-v3,node.kubernetes.io/kube-proxy-ds-ready=true,node.kubernetes.io/masq-agent-ds-ready=true,node.kubernetes.io/node-problem-detector-ds-ready=true,topology.kubernetes.io/zone=ru-central1-b,yandex.cloud/node-group-id=cat1eqqbh097tsk1lc1h,yandex.cloud/pci-topology=k8s,yandex.cloud/preemptible=false
cl1t52dqf6hns9qrt8io-ylim   Ready    <none>   4d11h   v1.26.2   10.129.0.12   <none>        Ubuntu 20.04.6 LTS   5.4.0-177-generic   containerd://1.6.28   beta.kubernetes.io/arch=amd64,beta.kubernetes.io/instance-type=standard-v3,beta.kubernetes.io/os=linux,failure-domain.beta.kubernetes.io/zone=ru-central1-b,homework=true,kubernetes.io/arch=amd64,kubernetes.io/hostname=cl1t52dqf6hns9qrt8io-ylim,kubernetes.io/os=linux,node.kubernetes.io/instance-type=standard-v3,node.kubernetes.io/kube-proxy-ds-ready=true,node.kubernetes.io/masq-agent-ds-ready=true,node.kubernetes.io/node-problem-detector-ds-ready=true,topology.kubernetes.io/zone=ru-central1-b,yandex.cloud/node-group-id=cat4j7ls25lg207s6ani,yandex.cloud/pci-topology=k8s,yandex.cloud/preemptible=false

#Argocd pods

NAME                                                   READY   STATUS    RESTARTS        AGE
my-argocd-application-controller-0                     1/1     Running   0               3d10h
my-argocd-applicationset-controller-86894887b5-qfvwk   1/1     Running   1 (9m49s ago)   3d10h
my-argocd-dex-server-8459b894d7-dfzpt                  1/1     Running   0               3d10h
my-argocd-notifications-controller-6cf8564fdb-shnln    1/1     Running   0               3d10h
my-argocd-redis-65f69bb89c-tkzq6                       1/1     Running   0               3d10h
my-argocd-repo-server-65bdf9596c-4pztq                 1/1     Running   0               3d10h
my-argocd-server-64955d4d65-hb2d4                      1/1     Running   0               3d10h

#projects
NAME   AGE
otus   8d

kubectl apply -f app-networks.yaml
curl -I --resolve "homework.otus:80:51.250.35.31" -i http://homework.otus
HTTP/1.1 200 OK

#Ingress
NAME             CLASS   HOSTS           ADDRESS        PORTS   AGE
ingress-nginx1   nginx   homework.otus   51.250.35.31   80      3m37s

kubectl apply -f app-templating.yaml
curl -I --resolve "homework-templating.otus:80:51.250.35.31" -i http://homework-templating.otus
HTTP/1.1 200 OK

NAME                                           READY   STATUS    RESTARTS   AGE
nginx-kubernetes-templating-748df88c48-6btww   1/1     Running   0          7m37s
nginx-kubernetes-templating-748df88c48-dz9md   1/1     Running   0          7m37s
nginx-kubernetes-templating-748df88c48-p5bj7   1/1     Running   0          7m37s