### General

- ヒストグラムのラベルが下のテーブルに突き抜ける (テーブルにマウスオーバーしたとき). [リンク](https://togodx.dbcls.jp/human/?dataset=ensembl_gene&annotations=%5B%7B%22attribute%22%3A%22disease_diseases_mesh%22%7D%5D&filters=%5B%7B%22attribute%22%3A%22gene_chromosome_ensembl%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%2215%22%7D%5D%7D%5D)

- View resultsの画面で, ブラウザウィンドウの横幅を狭めると、部分的にトップの画面が見える. [リンク](https://togodx.dbcls.jp/human/?dataset=ensembl_gene&annotations=%5B%7B%22attribute%22%3A%22gene_high_level_expression_refex%22%7D%5D&filters=%5B%7B%22attribute%22%3A%22gene_chromosome_ensembl%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%2224%22%7D%5D%7D%5D)

- View resultsの画面で全部のデータを取得される前に, Returnでトップに戻り別の検索をすると, 異なるIDが混ざって表示される. [リンク](https://togodx.dbcls.jp/human/?dataset=ncbigene&annotations=%5B%7B%22attribute%22%3A%22gene_high_level_expression_refex%22%7D%5D&filters=%5B%7B%22attribute%22%3A%22compound_chemical_role_chebi%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%2278298%22%7D%5D%7D%5D)
  - (結果が全部出ないうちにReturnで戻り, TargetだけNCBI geneからGlyTouCanに変えて再びView resultsすると, 上の方の行だけGlyToucanで, あとはNCBI Geneが表示されていたりする.)

- View resultの画面で, 結果が0件 (No Data Found) だが, 矢印がずっとくるくる回っている. [リンク](https://togodx.dbcls.jp/human/?dataset=nando&annotations=%5B%7B%22attribute%22%3A%22compound_action_type_chembl%22%7D%5D&filters=%5B%7B%22attribute%22%3A%22compound_drug_indication_mesh_chembl%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%22D007239%22%7D%5D%7D%2C%7B%22attribute%22%3A%22interaction_chembl_assay_existence_uniprot%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%221%22%7D%5D%7D%5D)

- View resultsの画面で, ヒストグラムの数字とテーブルが合わないことがある. 例: ヒストグラムだと Mendelian diseaseが2件だが, テーブルの中を見ると Mendelian diseaseが3件. [リンク](https://togodx.dbcls.jp/human/?dataset=ensembl_gene&annotations=%5B%7B%22attribute%22%3A%22disease_diseases_mondo%22%7D%5D&filters=%5B%7B%22attribute%22%3A%22gene_biotype_ensembl%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%22miRNA%22%7D%5D%7D%5D)

- ダウンロードされるTSVファイルの中身は, 画面の表示と合っている? [リンク](https://togodx.dbcls.jp/human/?dataset=ensembl_gene&annotations=%5B%7B%22attribute%22%3A%22gene_high_level_expression_refex%22%7D%5D&filters=%5B%7B%22attribute%22%3A%22variant_clinical_significance_togovar%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%22risk_factor%22%7D%5D%7D%5D)

### 個別のバーに関するコメント

- `# of interacting proteins` にマップされなくなっている? [リンク](https://togodx.dbcls.jp/human/?dataset=chembl_compound&annotations=%5B%7B%22attribute%22%3A%22interaction_number_of_interacting_proteins_uniprot%22%7D%2C%7B%22attribute%22%3A%22interaction_chembl_assay_existence_uniprot%22%7D%5D&filters=%5B%7B%22attribute%22%3A%22disease_diseases_mesh%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%22D007239%22%7D%5D%7D%5D)

## 解決済

- View resultsの画面のヒストグラムは, 決まった順で並んだ方が見やすいのでは (chr1, chr2, … 等) [リンク](https://togodx.dbcls.jp/human/?dataset=mesh&annotations=%5B%7B%22attribute%22%3A%22gene_chromosome_ensembl%22%7D%5D&filters=%5B%7B%22attribute%22%3A%22disease_diseases_mesh%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%22D009422%22%7D%5D%7D%5D)

- View resultsの画面でしばらく時間がかかり, Bad Gateway (502) と出ることがある (GOにマップしたときなど) [リンク](https://togodx.dbcls.jp/human/?dataset=ensembl_gene&annotations=%5B%7B%22attribute%22%3A%22protein_biological_process_uniprot%22%7D%5D&filters=%5B%7B%22attribute%22%3A%22protein_domains_uniprot%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%22393%22%7D%5D%7D%5D)

- View resultsの画面でしばらく時間がかかり, timeout of 120000ms exceeded と出ることがある. [リンク](https://togodx.dbcls.jp/human/?dataset=ensembl_gene&annotations=%5B%7B%22attribute%22%3A%22protein_isolation_source_uniprot%22%7D%5D&filters=%5B%7B%22attribute%22%3A%22gene_chromosome_ensembl%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%2224%22%7D%5D%7D%5D)
