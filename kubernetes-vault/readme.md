Установка consul
helm install consul hashicorp/consul -n consul
helm upgrade --install consul -f consul_values.yaml hashicorp/consul -n consul

Установка vault
helm install vault -f vault_values.yaml hashicorp/vault -n vault

kubectl -n vault exec -ti vault-0 -- /bin/sh -c "vault operator init -key-shares=3 -key-threshold=2"

kubectl port-forward vault-0 8200:8200

создаем авторизацию kubernetes
$ vault auth enable kubernetes

добавляем vault kubernetes
vault write auth/kubernetes/config \
        token_reviewer_jwt="$TOKEN_REVIEW_JWT" \
        kubernetes_host=$ADDR_HOST \
        kubernetes_ca_cert=@ca.crt

добавляем политику
Key      Value
---      -----
name     otus-policy
rules    path "otus/*" {
  capabilities = ["read", "list"]
}

добавляем роль для SA vault-auth
Key                                         Value
---                                         -----
alias_name_source                           serviceaccount_uid
bound_service_account_names                 [vault-auth]
bound_service_account_namespace_selector    n/a
bound_service_account_namespaces            [vault]
policies                                    [otus-policy]
token_bound_cidrs                           []
token_explicit_max_ttl                      0s
token_max_ttl                               0s
token_no_default_policy                     false
token_num_uses                              0
token_period                                0s
token_policies                              [otus-policy]
token_ttl                                   1h
token_type                                  default
ttl                                         1h


Установкка External-secret
helm repo add external-secrets https://charts.external-secrets.io
helm install external-secrets external-secrets/external-secrets -n vault

создаем externalsecret
kubectl apply -f external-secret/externalsecret.yaml

NAME                 AGE   STATUS   CAPABILITIES   READY
vault-secret-store   39m   Valid    ReadWrite      True

NAME           STORE                REFRESH INTERVAL   STATUS         READY
vault-secret   vault-secret-store   5s                 SecretSynced   True

проверяем наличие секрета otus-cred
kubectl -n vault get secret otus-cred

NAME        TYPE     DATA   AGE
otus-cred   Opaque   2      42m

apiVersion: v1
data:
  password: YXNhamtqa2Focw==
  username: b3R1cw==
immutable: false
kind: Secret