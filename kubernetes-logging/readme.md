1)
helm repo add grafana https://grafana.github.io/helm-charts
2)
kubectl create -n logging
3)
helm install -n logging loki --values values.yaml grafana/loki


kubectl get nodes -o custom-columns=NAME:.metadata.name,TAINTS:.spec.taints
NAME                        TAINTS
cl19jdq4f34mf9f213r5-osyz   [map[effect:NoSchedule key:node-role value:infra]]
cl1t52dqf6hns9qrt8io-izel   <none>


kubectl get node -o wide --show-labels 
NAME                        STATUS   ROLES    AGE    VERSION   INTERNAL-IP   EXTERNAL-IP      OS-IMAGE             KERNEL-VERSION      CONTAINER-RUNTIME     LABELS
cl19jdq4f34mf9f213r5-osyz   Ready    <none>   5d3h   v1.26.2   10.129.0.33   158.160.73.157   Ubuntu 20.04.6 LTS   5.4.0-174-generic   containerd://1.6.28   beta.kubernetes.io/arch=amd64,beta.kubernetes.io/instance-type=standard-v3,beta.kubernetes.io/os=linux,failure-domain.beta.kubernetes.io/zone=ru-central1-b,kubernetes.io/arch=amd64,kubernetes.io/hostname=cl19jdq4f34mf9f213r5-osyz,kubernetes.io/os=linux,node-group-name=infra,node.kubernetes.io/instance-type=standard-v3,node.kubernetes.io/kube-proxy-ds-ready=true,node.kubernetes.io/masq-agent-ds-ready=true,node.kubernetes.io/node-problem-detector-ds-ready=true,topology.kubernetes.io/zone=ru-central1-b,yandex.cloud/node-group-id=cat1eqqbh097tsk1lc1h,yandex.cloud/pci-topology=k8s,yandex.cloud/preemptible=false
cl1t52dqf6hns9qrt8io-izel   Ready    <none>   6d2h   v1.26.2   10.129.0.14   84.201.141.45    Ubuntu 20.04.6 LTS   5.4.0-174-generic   containerd://1.6.28   beta.kubernetes.io/arch=amd64,beta.kubernetes.io/instance-type=standard-v3,beta.kubernetes.io/os=linux,failure-domain.beta.kubernetes.io/zone=ru-central1-b,kubernetes.io/arch=amd64,kubernetes.io/hostname=cl1t52dqf6hns9qrt8io-izel,kubernetes.io/os=linux,node.kubernetes.io/instance-type=standard-v3,node.kubernetes.io/kube-proxy-ds-ready=true,node.kubernetes.io/masq-agent-ds-ready=true,node.kubernetes.io/node-problem-detector-ds-ready=true,topology.kubernetes.io/zone=ru-central1-b,yandex.cloud/node-group-id=cat4j7ls25lg207s6ani,yandex.cloud/pci-topology=k8s,yandex.cloud/preemptible=false

4)
kubectl create namespace monitoring
helm install grafana grafana/grafana --namespace monitoring

5)
kubectl get secret --namespace monitoring grafana -o jsonpath="{.data.admin-password}" | base64 --decode ; echo


kubectl get pod -n monitoring
NAME                       READY   STATUS    RESTARTS   AGE
grafana-77df5f6896-sqrks   1/1     Running   0          2m11s
kubectl port-forward grafana-77df5f6896-sqrks 3000:3000

