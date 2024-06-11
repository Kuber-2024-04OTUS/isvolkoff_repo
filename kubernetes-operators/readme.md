Проверка:
Запускаем sa.yaml, full-access.yaml, deployment.yaml, custom_obj.yaml

- pvc
NAME            STATUS   VOLUME         CAPACITY   ACCESS MODES   STORAGECLASS   VOLUMEATTRIBUTESCLASS   AGE
new-mysql-pvc   Bound    new-mysql-pv   1Gi        RWO            standard       <unset>                 64s

- pv
NAME           CAPACITY   ACCESS MODES   RECLAIM POLICY   STATUS   CLAIM                   STORAGECLASS   VOLUMEATTRIBUTESCLASS   REASON   AGE
new-mysql-pv   1Gi        RWO            Retain           Bound    default/new-mysql-pvc   standard       <unset>                          21s

- mysql
NAME        AGE
new-mysql   94s

- deployment
NAME           READY   UP-TO-DATE   AVAILABLE   AGE
mysql-deploy   1/1     1            1           2m20s
new-mysql      1/1     1            1           2m2s

Проверка задания со *:

- mysqls
NAME        AGE
new-mysql   2m15s

- pvc
NAME            STATUS   VOLUME         CAPACITY   ACCESS MODES   STORAGECLASS   VOLUMEATTRIBUTESCLASS   AGE
new-mysql-pvc   Bound    new-mysql-pv   1Gi        RWO            standard       <unset>                 8m40s

- service
NAME         TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)    AGE
kubernetes   ClusterIP   10.96.0.1    <none>        443/TCP    32d
new-mysql    ClusterIP   None         <none>        3306/TCP   8m54s

- deployment
NAME           READY   UP-TO-DATE   AVAILABLE   AGE
mysql-deploy   1/1     1            1           2m20s
new-mysql      1/1     1            1           2m2s

Проверка задания с **

- service
NAME           TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)    AGE
kubernetes     ClusterIP   10.96.0.1      <none>        443/TCP    33d
svc-hw-mysql   ClusterIP   10.96.63.186   <none>        3306/TCP   50s
- deployment
 NAME              READY   UP-TO-DATE   AVAILABLE   AGE
deploy-hw-mysql   1/1     1            1           90s
- pvc
NAME           STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS   VOLUMEATTRIBUTESCLASS   AGE
pvc-hw-mysql   Bound    pvc-c67db30c-8dcc-47c3-b112-33ec17a9c45b   1G         RWO            standard       <unset>                 2m13s

kubectl delete mysqls hw-mysql
- deployment
 NAME              READY   UP-TO-DATE   AVAILABLE   AGE
- service
NAME           TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)    AGE
kubernetes     ClusterIP   10.96.0.1      <none>        443/TCP    33d 