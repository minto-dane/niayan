# この版の検査方法と限界

現行の検査は3種類です。

`reference-checks.json`: 独立したPythonによるpolicy例・限定列挙・health frame形式/暗号fixture検査。Ada実装を実行していません。計算モデルとAda実装の同値性や、実クラスタの性質を証明するものではありません。

`native-primitive-probes.json`: 0700の一時scratch内で、ファイルfsync/rename、排他flock、symlink拒否、partial tail保存後truncateをLinux APIで確認しました。MC_FS/MC_LogのAdaを実行しておらず、実電源断やディスクが嘘をつく故障も試験していません。host service、network cluster、fence、rebootを操作していません。

`source-checks.json`: byte-for-byte vendor/profile、実際のPOSIX source checkerによる改変/欠落/未知/symlink/special/duplicate拒否、シェルsyntax、GPRのsource/main存在、重要guardへの参照を確認しました。静的な文字列存在を意味的安全性の証明として数えていません。各checkのscopeをJSONに明記しています。

実際の`make compile-all/test/flow/prove`試行は`build-proof-attempts.json`とlogに残しました。gprbuild/GNATproveがなく、Ada build/test/proofはNOT_RUN_MISSING_TOOLCHAINです。前版evidenceは`history-expanded-v2/`に移動し、新sourceの実行成功と誤認しないようにしました。

配布時には全manifest、ZIPのCRC/path/内容digestを再照合します。manifestとSHA256は改変検出用で、独立したrelease署名や公開鍵信頼を作りません。

参照検査・一時生成に使ったPythonは開発中の補助であり、本番runtimeや配布コードへ含めていません。再実行するための正式なsource側の試験は各Ada testsとciにあります。未実行のAda試験を再現済みと表示しません。
