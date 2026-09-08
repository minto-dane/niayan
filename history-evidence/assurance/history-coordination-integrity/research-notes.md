# Primary-source review used for this change

Accessed 2026-09-06. These sources explain external contracts; they do not verify Mission Core.
No third-party implementation code is imported by this edition.

- etcd API guarantees: https://etcd.io/docs/v3.6/learning/api_guarantees/ — linearizability, transactions, response/failure limits. The Mission Core guard transaction is a design built on those guarantees, not an external-resource lock.
- etcd API fields: https://etcd.io/docs/v3.6/learning/api/ — response cluster/member identity and revisions, transactions and key metadata.
- etcdctl native JSON printer, inspected tag: https://github.com/etcd-io/etcd/blob/etcdctl/v3.6.10/etcdctl/ctlv3/command/printer_json.go — uses Go encoding/json.
- etcdctl dispatch printer: https://github.com/etcd-io/etcd/blob/etcdctl/v3.6.10/etcdctl/ctlv3/command/printer.go — transaction response supplied to JSON printing.
- generated protocol types: https://pkg.go.dev/go.etcd.io/etcd/api/v3/etcdserverpb — ResponseOp.Response / ResponseOp_ResponsePut.ResponsePut structure. Together with the native printer this is the basis for the strict native JSON fixture shape. It was NOT captured from an executed etcdctl here.
- gRPC gateway: https://etcd.io/docs/v3.6/dev-guide/api_grpc_gateway/ — a different JSON/proto mapping; not interchangeable with the chosen native CLI output.
- SPARK boundary assumptions: https://docs.adacore.com/spark2014-docs/html/ug/en/usage_scenarios.html — proof levels and assumptions for unverified code. This release has not run GNATprove.

Pinned binary acceptance and actual server/client compatibility still require native tests on the target supported distribution. A reviewed tag is a format reference, not a claim that the binary was acquired, executed, or qualified.
