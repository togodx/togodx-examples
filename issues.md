### General

- ヒストグラムのラベルが下のテーブルに突き抜ける (テーブルにマウスオーバーしたとき). [リンク](https://togodx.dbcls.jp/human/?dataset=ensembl_gene&annotations=%5B%7B%22attribute%22%3A%22disease_diseases_mesh%22%7D%5D&filters=%5B%7B%22attribute%22%3A%22gene_chromosome_ensembl%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%2215%22%7D%5D%7D%5D)

- View resultsの画面で, ブラウザウィンドウの横幅を狭めると、部分的にトップの画面が見える. [リンク](https://togodx.dbcls.jp/human/?dataset=ensembl_gene&annotations=%5B%7B%22attribute%22%3A%22gene_high_level_expression_refex%22%7D%5D&filters=%5B%7B%22attribute%22%3A%22gene_chromosome_ensembl%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%2224%22%7D%5D%7D%5D)

- View resultsの画面で全部のデータを取得される前に, Returnでトップに戻り別の検索をすると, 異なるIDが混ざって表示される (Pauseをかけても. 結果が全部取得されてからだと, 正しく表示される). [リンク](https://togodx.dbcls.jp/human/?dataset=ncbigene&annotations=%5B%7B%22attribute%22%3A%22gene_high_level_expression_refex%22%7D%5D&filters=%5B%7B%22attribute%22%3A%22compound_chemical_role_chebi%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%2278298%22%7D%5D%7D%5D)
    - 結果が全部出ないうちにReturnで戻り, TargetだけNCBI geneからGlyTouCanに変えて再びView resultsした結果が下図. 最初の1行だけGlyToucanの結果で, あとはNCBI Gene.

- View resultの画面で, 結果が0件 (No Data Found) だが, 矢印がずっとくるくる回っている. [リンク](https://togodx.dbcls.jp/human/?dataset=nando&annotations=%5B%7B%22attribute%22%3A%22compound_action_type_chembl%22%7D%5D&filters=%5B%7B%22attribute%22%3A%22compound_drug_indication_mesh_chembl%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%22D007239%22%7D%5D%7D%2C%7B%22attribute%22%3A%22interaction_chembl_assay_existence_uniprot%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%221%22%7D%5D%7D%5D)

- View resultsの画面で, ヒストグラムの数字とテーブルが合わないことがある. 例: ヒストグラムだと Mendelian diseaseが2件だが, テーブルの中を見ると Mendelian diseaseが3件. [リンク](https://togodx.dbcls.jp/human/?dataset=ensembl_gene&annotations=%5B%7B%22attribute%22%3A%22disease_diseases_mondo%22%7D%5D&filters=%5B%7B%22attribute%22%3A%22gene_biotype_ensembl%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%22miRNA%22%7D%5D%7D%5D)

### 個別のバーに関するコメント

- 階層構造をクリックして下がっていったときに、三角マークはあるが、開くと中身がないことがある.
    - Diseases in MeSH -> Nervous System Diseases -> Demyelinating Diseases
- MeSHの階層をクリックしていっても, Alzheimer diseaseが出てこない
    - 末端のリーフは、階層構造には出てこない
    - （Alzheimer diseaseは該当しないが）Schizophreniaなど、[MeSH Tree](https://meshb.nlm.nih.gov/treeView)上でDiseases [C] の下にはなくて[Mental Disorders [F03]](https://meshb.nlm.nih.gov/record/ui?ui=D001523) の下にのみある疾患もあり、現行のバーでは出てこない

### null問題

- View resultsの画面で, MeSHがC番号のときに, ラベルがnullになる. メタスタンザではラベルが取得できている. [リンク](https://togodx.dbcls.jp/human/?dataset=mesh&annotations=%5B%7B%22attribute%22%3A%22disease_diseases_mesh%22%7D%5D&filters=%5B%7B%22attribute%22%3A%22gene_chromosome_ensembl%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%2215%22%7D%5D%7D%5D)
- 結果画面でchebi番号の後がnullになっているものがあるが、chebi番号をクリックしてみるとlabelは付いている。(labelが付けられるはず?)
- NCBI GeneをTargetにしても結果表のラベルがnullになることがある。メタスタンザで詳細情報を表示するとMetaStanza API errorとなっている
- 化合物データベース(Chebi, ChEMBL, Pubchem)をtargetに選んだ場合、結果表でのラベルが”null”になるのだが、メタスタンザで詳細情報を表示するとラベルがある

### その他のコメント

- View resultsの画面で, ヒストグラムが横方向に長いことがある. 例: # of Interacting proteins のヒストグラムが横に伸びていって, ChEMBL Assay Existenceが見えなくなる. [リンク](https://togodx.dbcls.jp/human/?dataset=chembl_compound&annotations=%5B%7B%22attribute%22%3A%22interaction_number_of_interacting_proteins_uniprot%22%7D%2C%7B%22attribute%22%3A%22interaction_chembl_assay_existence_uniprot%22%7D%5D&filters=%5B%7B%22attribute%22%3A%22disease_diseases_mesh%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%22D007239%22%7D%5D%7D%5D)
    - (Barの画面でChEMBL Assay Existenceを先に指定すると順番が変わってChEMBL Assay Existenceが見えるようになる)
- Saved Conditionに表示された数と、ヒストグラムに表示された数がずれるのはどういうときで、なぜそうなるのか[例](https://togodx.dbcls.jp/human/?dataset=ensembl_gene&annotations=%5B%7B%22attribute%22%3A%22gene_high_level_expression_refex%22%7D%5D&filters=%5B%7B%22attribute%22%3A%22variant_clinical_significance_togovar%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%22risk_factor%22%7D%5D%7D%5D)

## 解決済

- View resultsの画面のヒストグラムは, 決まった順で並んだ方が見やすいのでは (chr1, chr2, … 等) [リンク](https://togodx.dbcls.jp/human/?dataset=mesh&annotations=%5B%7B%22attribute%22%3A%22gene_chromosome_ensembl%22%7D%5D&filters=%5B%7B%22attribute%22%3A%22disease_diseases_mesh%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%22D009422%22%7D%5D%7D%5D)

- View resultsの画面でしばらく時間がかかり, Bad Gateway (502) と出ることがある (GOにマップしたときなど) [リンク](https://togodx.dbcls.jp/human/?dataset=ensembl_gene&annotations=%5B%7B%22attribute%22%3A%22protein_biological_process_uniprot%22%7D%5D&filters=%5B%7B%22attribute%22%3A%22protein_domains_uniprot%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%22393%22%7D%5D%7D%5D)

- View resultsの画面でしばらく時間がかかり, timeout of 120000ms exceeded と出ることがある. [リンク](https://togodx.dbcls.jp/human/?dataset=ensembl_gene&annotations=%5B%7B%22attribute%22%3A%22protein_isolation_source_uniprot%22%7D%5D&filters=%5B%7B%22attribute%22%3A%22gene_chromosome_ensembl%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%2224%22%7D%5D%7D%5D)
