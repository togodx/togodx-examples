## 既存バーの動作と有用性検証の試行

- 記載例
    - [ミトコンドリアゲノム由来のタンパク質をターゲットとする薬とその適用疾患](http://ep.dbcls.jp/togodx-server-pg-dev/build/?dataset=chebi&annotations=%5B%7B%22attribute%22%3A%22disease_diseases_mesh%22%7D%5D&filters=%5B%7B%22attribute%22%3A%22gene_chromosome_ensembl%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%2225%22%7D%5D%7D%2C%7B%22attribute%22%3A%22interaction_chembl_assay_existence_uniprot%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%221%22%7D%5D%7D%5D)(信定)
        - target dataset:
            - chebi_compound
        - filter1:
            - chembl_assay_existance > conf_score-9
                - (chebi_compound→chembl_compound→chemblでconfidence=9）
        - filter2:
            - chromosome > MT
                - (chebi_compound→chembl_compound→chembl_target→genes in MT)
        - map:
            - diseases in mesh
        - comments
            - comment
- 小野
    - [免疫グロブリンドメインを持つタンパク質をコードする遺伝子のGO(Biological process)一覧](http://ep.dbcls.jp/togodx-server-pg-dev/build/?dataset=ensembl_gene&annotations=%5B%7B%22attribute%22%3A%22protein_biological_process_uniprot%22%7D%5D&filters=%5B%7B%22attribute%22%3A%22protein_domains_uniprot%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%22393%22%7D%5D%7D%5D)
        - target dataset:
            - ensembl_gene
        - filter1:
            - Protein domains > Immunoglobulin domain
        - map:
            - Biological process
        - comments
            - timeout of 120000ms exceeded になる
            - 上位階層をMapしてもあまり解釈できることが少ない
            - (2022/03/16 hono 追記)高速版では解消
- 信定、建石
    - [環境汚染物質がターゲットとする遺伝子がどこで高発現しているか](http://ep.dbcls.jp/togodx-server-pg-dev/build/?dataset=ensembl_gene&annotations=%5B%7B%22attribute%22%3A%22gene_high_level_expression_refex%22%7D%5D&filters=%5B%7B%22attribute%22%3A%22compound_chemical_role_chebi%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%2278298%22%7D%5D%7D%5D)
        - target dataset:
            - ensembl_gene
        - filter1:
            - Chemical role > environmental contaminant
        - map:
            - Tissue-specific high expression (RefEx GeneChip)
        - comments
            - 特に問題なく実行できた
    - [疾患に関与する環境汚染物質](http://ep.dbcls.jp/togodx-server-pg-dev/build/?dataset=chebi&annotations=%5B%7B%22attribute%22%3A%22disease_diseases_mesh%22%7D%5D&filters=%5B%7B%22attribute%22%3A%22compound_chemical_role_chebi%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%2278298%22%7D%5D%7D%5D)
        - target:
            - CHEBI compound
        - filter:
            - Chemical role > environmental contaminant
        - map:
            - Disease in MeSH
        - comment
            - 実行は問題なし、ただ実害はありませんが、結果の画面で上の方の結果にマウスオーバーするとヒストグラムのラベルの一部？？が出てきます(下図黄色い部分の斜めの文字列）
        -

            ![TogoDX%E3%82%A2%E3%83%88%E3%83%AA%E3%83%92%209256c/image9.png](TogoDX%E3%82%A2%E3%83%88%E3%83%AA%E3%83%92%209256c/image9.png)

    - [環境汚染物質が薬として役立つ疾患](http://ep.dbcls.jp/togodx-server-pg-dev/build/?dataset=mesh&annotations=%5B%7B%22attribute%22%3A%22disease_diseases_mesh%22%7D%5D&filters=%5B%7B%22attribute%22%3A%22compound_chemical_role_chebi%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%2278298%22%7D%5D%7D%5D)
        - 最初「環境汚染物質で引き起こされる」疾患としていましたが、Chemical→DiseaseはDrug Indicationでしかつながっていないはずなので上の解釈になるのではないかと思います
        - target:
            - MeSH
        - filter、map
            - 上と同じ
        - comment
            - Disease in MeSHのカラムが空欄になっている結果の解釈がよくわかりません。

> Disease in MeSH にリンクのない物質、かと思いましたが、一番左のMeSHによってリストされている物質が異なっているようですし。
>
- [目的の反応にcomponentとして参加する化合物とタンパク質をリストし、そのタンパク質の構造が解析されているかどうかを調べる](http://ep.dbcls.jp/togodx-server-pg-dev/build/?dataset=chebi&annotations=%5B%7B%22attribute%22%3A%22structure_data_existence_uniprot%22%7D%5D&filters=%5B%7B%22attribute%22%3A%22interaction_proteins_in_pathway_reactome%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%22R-HSA-2162123%22%2C%22path%22%3A%5B%22R-HSA-1430728%22%2C%22R-HSA-556833%22%2C%22R-HSA-8978868%22%2C%22R-HSA-2142753%22%5D%7D%5D%7D%2C%7B%22attribute%22%3A%22interaction_compounds_in_pathway_reactome%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%22R-HSA-2162123%22%2C%22path%22%3A%5B%22R-HSA-1430728%22%2C%22R-HSA-556833%22%2C%22R-HSA-8978868%22%2C%22R-HSA-2142753%22%5D%7D%5D%7D%5D)
    - target:
        - chebi_compound
    - filter1
        - compounds in pathway >Metabolism >Metabolism of lipids >Fatty acid metabolism >Arachidonic acid metabolism >Synthesis of Prostaglandins (PG) and Thromboxanes (TX)
    - filter2
        - proteins in pathway > （filtter1と同じ）
    - comment
        - 結果でreactome_pathwayのIDが取れない
- [薬効のある化粧品（香料含む）](http://ep.dbcls.jp/togodx-server-pg-dev/build/?dataset=pubchem_compound&annotations=%5B%5D&filters=%5B%7B%22attribute%22%3A%22compound_application_type_chebi%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%2248318%22%7D%2C%7B%22node%22%3A%2264857%22%7D%5D%7D%2C%7B%22attribute%22%3A%22compound_drug_indication_mesh_chembl%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%22D009369%22%7D%2C%7B%22node%22%3A%22D005261%22%7D%2C%7B%22node%22%3A%22D002318%22%7D%2C%7B%22node%22%3A%22D017437%22%7D%2C%7B%22node%22%3A%22D013568%22%7D%2C%7B%22node%22%3A%22D007239%22%7D%2C%7B%22node%22%3A%22D006425%22%7D%2C%7B%22node%22%3A%22D007154%22%7D%2C%7B%22node%22%3A%22D009750%22%7D%2C%7B%22node%22%3A%22D009358%22%7D%2C%7B%22node%22%3A%22D009422%22%7D%2C%7B%22node%22%3A%22D004066%22%7D%2C%7B%22node%22%3A%22D004700%22%7D%2C%7B%22node%22%3A%22D012140%22%7D%2C%7B%22node%22%3A%22D064419%22%7D%2C%7B%22node%22%3A%22D005128%22%7D%2C%7B%22node%22%3A%22D014947%22%7D%2C%7B%22node%22%3A%22D009140%22%7D%2C%7B%22node%22%3A%22D009057%22%7D%2C%7B%22node%22%3A%22D010038%22%7D%2C%7B%22node%22%3A%22D052801%22%7D%2C%7B%22node%22%3A%22D009784%22%7D%2C%7B%22node%22%3A%22D000820%22%7D%5D%7D%5D)
    - target:
        - Pubchem compound
    - filter 1:
        - Application type > fragranceとcosmetic
    - filter 2:
        - Drug indicationの全ての項目にチェックを入れた
    - comment
        - resultのPubchem Compoundのラベルがnullになっていることがある。詳細画面

            ![TogoDX%E3%82%A2%E3%83%88%E3%83%AA%E3%83%92%209256c/image8.png](TogoDX%E3%82%A2%E3%83%88%E3%83%AA%E3%83%92%209256c/image8.png)

- inhibitorとして働く化合物をリストし、適応疾患にマップする
    - targetを下記にした場合のリンク
        - [chebi](http://ep.dbcls.jp/togodx-server-pg-dev/build/?dataset=chebi&annotations=%5B%7B%22attribute%22%3A%22compound_drug_indication_mesh_chembl%22%7D%5D&filters=%5B%7B%22attribute%22%3A%22compound_biological_role_chebi%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%2235222%22%7D%5D%7D%5D) (318件), [chembl](http://ep.dbcls.jp/togodx-server-pg-dev/build/?dataset=chembl_compound&annotations=%5B%7B%22attribute%22%3A%22compound_drug_indication_mesh_chembl%22%7D%5D&filters=%5B%7B%22attribute%22%3A%22compound_biological_role_chebi%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%2235222%22%7D%5D%7D%5D) (217件), [pubchem](http://ep.dbcls.jp/togodx-server-pg-dev/build/?dataset=chebi&annotations=%5B%7B%22attribute%22%3A%22compound_drug_indication_mesh_chembl%22%7D%5D&filters=%5B%7B%22attribute%22%3A%22compound_biological_role_chebi%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%2235222%22%7D%5D%7D%5D) (298件)
    - target:
        - chebi_compound
    - filter1
        - biological role > inhibitor
    - map
        - drug indication
    - comment
        - targetをchebi, pubchemにするとnullがたくさんでる
- 疾患に対してinhibitorとして働く化合物をリストし、薬としての開発段階を確認する
    - targetを下記にした場合のリンク
        - [mondo](http://ep.dbcls.jp/togodx-server-pg-dev/build/?dataset=mondo&annotations=%5B%7B%22attribute%22%3A%22compound_drug_development_phase_chembl%22%7D%5D&filters=%5B%7B%22attribute%22%3A%22compound_action_type_chembl%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%22INHIBITOR%22%7D%5D%7D%5D) (958件), [mesh](http://ep.dbcls.jp/togodx-server-pg-dev/build/?dataset=mesh&annotations=%5B%7B%22attribute%22%3A%22compound_drug_development_phase_chembl%22%7D%5D&filters=%5B%7B%22attribute%22%3A%22compound_action_type_chembl%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%22INHIBITOR%22%7D%5D%7D%5D) (1262件), [nando](http://ep.dbcls.jp/togodx-server-pg-dev/build/?dataset=nando&annotations=%5B%7B%22attribute%22%3A%22compound_drug_development_phase_chembl%22%7D%5D&filters=%5B%7B%22attribute%22%3A%22compound_action_type_chembl%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%22INHIBITOR%22%7D%5D%7D%5D) (0件), [human phenotype ontology](http://ep.dbcls.jp/togodx-server-pg-dev/build/?dataset=hp&annotations=%5B%7B%22attribute%22%3A%22compound_drug_development_phase_chembl%22%7D%5D&filters=%5B%7B%22attribute%22%3A%22compound_action_type_chembl%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%22INHIBITOR%22%7D%5D%7D%5D) (112件)
    - filter1
        - action type > inhibitor
    - map
        - drug development phase
    - comment
- biomarkerとして働く化合物をリストし、どの疾患と関係しているかみたい（←できない）
    - targetを下記にした場合のリンク
        - [chebi](http://ep.dbcls.jp/togodx-server-pg-dev/build/?dataset=chebi&annotations=%5B%7B%22attribute%22%3A%22disease_diseases_mesh%22%7D%5D&filters=%5B%7B%22attribute%22%3A%22compound_application_type_chebi%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%2259163%22%2C%22path%22%3A%5B%2247867%22%5D%7D%5D%7D%5D) (56件)
    - filter1
        - application type > indicator > biomarker
    - map
        - diseases in mesh
    - comment
        - biomarkerの化合物はリストできるが、疾患と化合物はchemblの適応疾患で繋がっているので、意味がなくなってしまう。化合物が引き起こす疾患などのルートがあるといいかも。
- Nutritional and metabolic diseasesに効く薬についてATC分類を見る (pubchem ATC)
    - targetを下記にした場合のリンク
        - [chebi](http://ep.dbcls.jp/togodx-server-pg-dev/build/?dataset=chebi&annotations=%5B%7B%22attribute%22%3A%22compound_atc_classification_chembl%22%7D%5D&filters=%5B%7B%22attribute%22%3A%22disease_diseases_mesh%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%22D009750%22%7D%5D%7D%5D) (367件), [chembl](http://ep.dbcls.jp/togodx-server-pg-dev/build/?dataset=chembl_compound&annotations=%5B%7B%22attribute%22%3A%22compound_atc_classification_pubchem%22%7D%5D&filters=%5B%7B%22attribute%22%3A%22disease_diseases_mesh%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%22D009750%22%7D%5D%7D%5D) (646件), [pubchem](http://ep.dbcls.jp/togodx-server-pg-dev/build/?dataset=pubchem_compound&annotations=%5B%7B%22attribute%22%3A%22compound_atc_classification_pubchem%22%7D%5D&filters=%5B%7B%22attribute%22%3A%22disease_diseases_mesh%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%22D009750%22%7D%5D%7D%5D) (594件)
    - filter1
        - diseases in mesh > nutritional and metabolic diseases
    - map
        - pubchem ATC classification
    - comment
- Nutritional and metabolic diseasesに効く薬についてATC分類を見る (chembl ATC)
    - targetを下記にした場合のリンク
        - [chebi](http://ep.dbcls.jp/togodx-server-pg-dev/build/?dataset=chebi&annotations=%5B%7B%22attribute%22%3A%22compound_atc_classification_pubchem%22%7D%5D&filters=%5B%7B%22attribute%22%3A%22disease_diseases_mesh%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%22D009750%22%7D%5D%7D%5D) (367件), [chembl](http://ep.dbcls.jp/togodx-server-pg-dev/build/?dataset=chembl_compound&annotations=%5B%7B%22attribute%22%3A%22compound_atc_classification_chembl%22%7D%5D&filters=%5B%7B%22attribute%22%3A%22disease_diseases_mesh%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%22D009750%22%7D%5D%7D%5D) (646件), [pubchem](http://ep.dbcls.jp/togodx-server-pg-dev/build/?dataset=pubchem_compound&annotations=%5B%7B%22attribute%22%3A%22compound_atc_classification_chembl%22%7D%5D&filters=%5B%7B%22attribute%22%3A%22disease_diseases_mesh%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%22D009750%22%7D%5D%7D%5D) (594件)
    - filter1
        - diseases in mesh > nutritional and metabolic diseases
    - map
        - chembl ATC classification
- [どう働くかよくわかっていないけれど薬効が認められている物質、が取れないかなと思いました](http://ep.dbcls.jp/togodx-server-pg-dev/build/?dataset=mesh&annotations=%5B%5D&filters=%5B%7B%22attribute%22%3A%22compound_application_type_chebi%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%2252217%22%7D%5D%7D%2C%7B%22attribute%22%3A%22interaction_chembl_assay_existence_uniprot%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%22unclassified%22%7D%5D%7D%5D)
    - target: MeSH
    - filter:
        - Application Type ->pharmaceuticals
        - Chembl Assay Existence -> no assay
    - comment
        - 504 Gateway Timeout
- 千葉
    - [Y染色体の遺伝子の発現特異性](http://ep.dbcls.jp/togodx-server-pg-dev/build/?dataset=ensembl_gene&annotations=%5B%7B%22attribute%22%3A%22protein_isolation_source_uniprot%22%7D%5D&filters=%5B%7B%22attribute%22%3A%22gene_chromosome_ensembl%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%2224%22%7D%5D%7D%5D)
        - target
            - ENSG
        - comment
            - 最後まで取得完了できない
            - (2022/03/16追記)高速版では解消
    - [神経系疾患に関連する遺伝子が、どの染色体にあるか](http://ep.dbcls.jp/togodx-server-pg-dev/build/?dataset=mesh&annotations=%5B%7B%22attribute%22%3A%22gene_chromosome_ensembl%22%7D%5D&filters=%5B%7B%22attribute%22%3A%22disease_diseases_mesh%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%22D009422%22%7D%5D%7D%5D)
        - target
            - ENSG
        - comment
            - Chromesomeの順番が1から順になってくれた方が見やすい
    - [Chr15にある遺伝子に関連した病気](http://ep.dbcls.jp/togodx-server-pg-dev/build/?dataset=mesh&annotations=%5B%7B%22attribute%22%3A%22disease_diseases_mesh%22%7D%5D&filters=%5B%7B%22attribute%22%3A%22gene_chromosome_ensembl%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%2215%22%7D%5D%7D%5D)
        - target
            - MeSH
        - comment
            - ラベルがnullになる問題. SPARQLの変更で修正可能なはず?
            - 以下の例と、数を比べてみる. targetが変わると結果が変わる.
    - [Chr15にある遺伝子に関連した病気](http://ep.dbcls.jp/togodx-server-pg-dev/build/?dataset=ensembl_gene&annotations=%5B%7B%22attribute%22%3A%22disease_diseases_mesh%22%7D%5D&filters=%5B%7B%22attribute%22%3A%22gene_chromosome_ensembl%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%2215%22%7D%5D%7D%5D)
        - target
            - ENSG
        - comment
            - ヒストグラムのラベルが、下のテーブルに突き抜ける問題あり.
- 八塚
    - [構造タンパク質と遺伝子の染色体ごとの分布](http://ep.dbcls.jp/togodx-server-pg-dev/build/?dataset=ensembl_gene&annotations=%5B%7B%22attribute%22%3A%22gene_chromosome_ensembl%22%7D%5D&filters=%5B%7B%22attribute%22%3A%22structure_data_existence_uniprot%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%221%22%7D%5D%7D%5D)
        - target
            - ENSG/NCBI Gene/UniProt/PDB
        - filter
            - Structure -> Proteins with structure data
        - map
            - Gene -> Chromosome
        - comment
            - PDBをtargetにした場合、Pauseにしても処理が止まらない
                - 2022/03/16 hono追記　50000件取得できた(これもなにかの上限に引っかかってる?キリが良すぎてあやしい…)。Pauseでも止まる。が、取得後、ブラウザの動作が不安定になる。
                - [http://ep.dbcls.jp/togodx-server-kohan-pg/build/?dataset=pdb&annotations=%5B%7B%22attribute%22%3A%22gene_chromosome_ensembl%22%7D%5D&filters=%5B%7B%22attribute%22%3A%22structure_data_existence_uniprot%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%221%22%7D%5D%7D%5D](http://ep.dbcls.jp/togodx-server-kohan-pg/build/?dataset=pdb&annotations=%5B%7B%22attribute%22%3A%22gene_chromosome_ensembl%22%7D%5D&filters=%5B%7B%22attribute%22%3A%22structure_data_existence_uniprot%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%221%22%7D%5D%7D%5D)
    - alpha-helicesを〇〇個持つ[タンパク質と遺伝子の染色体ごとの分布](http://ep.dbcls.jp/togodx-server-pg-dev/build/?dataset=ensembl_gene&annotations=%5B%7B%22attribute%22%3A%22gene_chromosome_ensembl%22%7D%5D&filters=%5B%7B%22attribute%22%3A%22structure_number_of_alpha_helices_pdb%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%2229%22%7D%5D%7D%5D)
        - target
            - ENSG/NCBI Gene/UniProt/ChEBI/ChEMBL/PubChem/GlyTouCan/Mondo/MeSH/NANDO/HPO
        - filter
            - Structure -> # of alpha-helices
        - map
            - Gene -> Chromosome
        - comment
            - alpha-helicesの数で遺伝子を絞り込んだはずが、絞り込まれた遺伝子に対応するPDBエントリが全部ヒットしてしまうため、alpha-helices数の分布も表示されてしまい、混乱する。
    - alpha-helicesを〇〇個持つ[タンパク質と遺伝子の染色体ごとの分布](http://ep.dbcls.jp/togodx-server-pg-dev/build/?dataset=pdb&annotations=%5B%7B%22attribute%22%3A%22gene_chromosome_ensembl%22%7D%5D&filters=%5B%7B%22attribute%22%3A%22structure_number_of_alpha_helices_pdb%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%2231%22%7D%5D%7D%5D)
        - target
            - PDB
        - filter
            - Structure -> # of alpha-helices
        - map
            - Gene -> Chromosome
        - comment
            - 結果表の1つ目と2つ目のカラムが同じPDBエントリを指すが、filterによる絞り込みは正しく実現される
    - beta-sheetsを〇〇個持つ[タンパク質と遺伝子の染色体ごとの分布](http://ep.dbcls.jp/togodx-server-pg-dev/build/?dataset=ensembl_gene&annotations=%5B%7B%22attribute%22%3A%22gene_chromosome_ensembl%22%7D%5D&filters=%5B%7B%22attribute%22%3A%22structure_number_of_beta_sheets_pdb%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%2214%22%7D%5D%7D%5D)
        - target
            - ENSG/NCBI Gene/UniProt/ChEMBL/PubChem/Mondo/MeSH/NANDO/HPO
        - filter
            - Structure -> # of beta-sheets
        - map
            - Gene -> Chromosome
        - comment
            - beta-sheetsの数で遺伝子を絞り込んだはずが、絞り込まれた遺伝子に対応するPDBエントリが全部ヒットしてしまうため、beta-sheets数の分布も表示されてしまい、混乱する。
    - beta-sheetsを〇〇個持つ[タンパク質と遺伝子の染色体ごとの分布](http://ep.dbcls.jp/togodx-server-pg-dev/build/?dataset=pdb&annotations=%5B%7B%22attribute%22%3A%22gene_chromosome_ensembl%22%7D%5D&filters=%5B%7B%22attribute%22%3A%22structure_number_of_beta_sheets_pdb%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%2214%22%7D%5D%7D%5D)
        - target
            - PDB
        - filter
            - Structure -> # of beta-sheets
        - map
            - Gene -> Chromosome
        - comment
            - 結果表の1つ目と2つ目のカラムが同じPDBエントリを指すが、filterによる絞り込みは正しく実現される
    - タンパク質を〇〇個持つPDBエントリ[と遺伝子の染色体ごとの分布](http://ep.dbcls.jp/togodx-server-pg-dev/build/?dataset=ensembl_gene&annotations=%5B%7B%22attribute%22%3A%22gene_chromosome_ensembl%22%7D%5D&filters=%5B%7B%22attribute%22%3A%22structure_number_of_peptides_pdb%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%226%22%7D%5D%7D%5D)
        - target
            - ENSG/NCBI Gene/UniProt/ChEBI/ChEMBL/PubChem/Mondo/MeSH/NANDO/HPO
        - filter
            - Structure -> # of peptides in a PDB entry
        - map
            - Gene -> Chromosome
        - comment
            - ペプチドの数で遺伝子を絞り込んだはずが、絞り込まれた遺伝子に対応するPDBエントリが全部ヒットしてしまうため、ペプチド数の分布も表示されてしまい、混乱する。
    - タンパク質を〇〇個持つPDBエントリ[と遺伝子の染色体ごとの分布](http://ep.dbcls.jp/togodx-server-pg-dev/build/?dataset=pdb&annotations=%5B%7B%22attribute%22%3A%22gene_chromosome_ensembl%22%7D%5D&filters=%5B%7B%22attribute%22%3A%22structure_number_of_peptides_pdb%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%226%22%7D%5D%7D%5D)
        - target
            - PDB
        - filter
            - Structure -> # of peptides in a PDB entry
        - map
            - Gene -> Chromosome
        - comment
            - 結果表の1つ目と2つ目のカラムが同じPDBエントリを指すが、filterによる絞り込みは正しく実現される
    - [疾患に関連する構造タンパク質と遺伝子の染色体ごとの分布](http://ep.dbcls.jp/togodx-server-pg-dev/build/?dataset=mondo&annotations=%5B%7B%22attribute%22%3A%22gene_chromosome_ensembl%22%7D%5D&filters=%5B%7B%22attribute%22%3A%22structure_data_existence_uniprot%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%221%22%7D%5D%7D%5D)
        - target
            - Mondo/NANDO/MeSH/HPO
        - filter
            - Structure -> Proteins with structure data
        - map
            - Gene -> Chromosome
        - comment
            - HPO以外、Pauseにしても、処理が止まらない
            - 表ではMeSHが”null”になっているものでも、メタスタンザで詳細情報を表示するとラベルがある
            - (3/16信定）高速化版で試行。Mondo/NANDO/MeSH : 数十秒で返ってくる。Pauseも機能している。3308件/661件/1656件。
            - MeSH : [http://ep.dbcls.jp/togodx-server-kohan-pg/build/?dataset=mesh&annotations=%5B%7B%22attribute%22%3A%22gene_chromosome_ensembl%22%7D%5D&filters=%5B%7B%22attribute%22%3A%22structure_data_existence_uniprot%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%221%22%7D%5D%7D%5D](http://ep.dbcls.jp/togodx-server-kohan-pg/build/?dataset=mesh&annotations=%5B%7B%22attribute%22%3A%22gene_chromosome_ensembl%22%7D%5D&filters=%5B%7B%22attribute%22%3A%22structure_data_existence_uniprot%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%221%22%7D%5D%7D%5D)
            -
    - [〇〇という手法を使って同定したPDBエントリと遺伝子の染色体ごとの分布](http://ep.dbcls.jp/togodx-server-pg-dev/build/?dataset=pdb&annotations=%5B%7B%22attribute%22%3A%22gene_chromosome_ensembl%22%7D%5D&filters=%5B%7B%22attribute%22%3A%22structure_analysis_methods_pdb%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%2204%22%7D%5D%7D%5D)
        - target
            - PDB
        - filter
            - Structure -> Analysis methods
        - map
            - Gene -> Chromosome
        - comment
            - 結果表の1つ目と2つ目のカラムが同じPDBエントリを指すが、filterによる絞り込みは正しく実現される
    - [〇〇という手法を使って同定したPDBエントリと結合する化合物と遺伝子の染色体ごとの分布](http://ep.dbcls.jp/togodx-server-pg-dev/build/?dataset=chembl_compound&annotations=%5B%7B%22attribute%22%3A%22gene_chromosome_ensembl%22%7D%5D&filters=%5B%7B%22attribute%22%3A%22structure_analysis_methods_pdb%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%2204%22%7D%5D%7D%5D)
        - target
            - ChEMBL/PubChem
        - filter
            - Structure -> Analysis methods
        - map
            - Gene -> Chromosome
        - comment
    - [〇〇という手法を使って同定したPDBエントリに関連する疾患と遺伝子の染色体ごとの分布](http://ep.dbcls.jp/togodx-server-pg-dev/build/?dataset=nando&annotations=%5B%7B%22attribute%22%3A%22gene_chromosome_ensembl%22%7D%5D&filters=%5B%7B%22attribute%22%3A%22structure_analysis_methods_pdb%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%2204%22%7D%5D%7D%5D)
        - target
            - NANDO/HPO
        - filter
            - Structure -> Analysis methods
        - map
            - Gene -> Chromosome
    - 結果が返ってこない例
        - [リンク](http://ep.dbcls.jp/togodx-server-pg-dev/build/?dataset=chebi&annotations=%5B%7B%22attribute%22%3A%22gene_chromosome_ensembl%22%7D%5D&filters=%5B%7B%22attribute%22%3A%22structure_data_existence_uniprot%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%221%22%7D%5D%7D%5D)
            - target
                - ChEBI
            - filter
                - Structure -> Proteins with structure data
            - map
                - Gene -> Chromosome
            - comment
                - 結果の数(19089)は表示されるが、しばらくして”Bad Gateway(502)”エラーになる
                - (3/16信定）高速化版で返ってくるようになった。が、結果表示後重くて動かない。
                - [http://ep.dbcls.jp/togodx-server-kohan-pg/build/?dataset=chebi&annotations=%5B%7B%22attribute%22%3A%22gene_chromosome_ensembl%22%7D%5D&filters=%5B%7B%22attribute%22%3A%22structure_data_existence_uniprot%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%221%22%7D%5D%7D%5D](http://ep.dbcls.jp/togodx-server-kohan-pg/build/?dataset=chebi&annotations=%5B%7B%22attribute%22%3A%22gene_chromosome_ensembl%22%7D%5D&filters=%5B%7B%22attribute%22%3A%22structure_data_existence_uniprot%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%221%22%7D%5D%7D%5D)
                -
        - [リンク](http://ep.dbcls.jp/togodx-server-pg-dev/build/?dataset=chembl_compound&annotations=%5B%7B%22attribute%22%3A%22gene_chromosome_ensembl%22%7D%5D&filters=%5B%7B%22attribute%22%3A%22structure_data_existence_uniprot%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%221%22%7D%5D%7D%5D)
            - target
                - ChEMBL/PubChem
            - filter
                - Structure -> Proteins with structure data
            - map
                - Gene -> Chromosome
            - comment
                - すぐに”Gateway Timeout(504)”エラーになる
                - (3/16信定）ChEMBL, PubChem共に高速化版で試行。数分でGateway Time-out (504)。
                - [http://ep.dbcls.jp/togodx-server-kohan-pg/build/?dataset=pubchem_compound&annotations=%5B%7B%22attribute%22%3A%22gene_chromosome_ensembl%22%7D%5D&filters=%5B%7B%22attribute%22%3A%22structure_data_existence_uniprot%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%221%22%7D%5D%7D%5D](http://ep.dbcls.jp/togodx-server-kohan-pg/build/?dataset=pubchem_compound&annotations=%5B%7B%22attribute%22%3A%22gene_chromosome_ensembl%22%7D%5D&filters=%5B%7B%22attribute%22%3A%22structure_data_existence_uniprot%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%221%22%7D%5D%7D%5D)
                -
                - [リンク](http://ep.dbcls.jp/togodx-server-pg-dev/build/?dataset=glytoucan&annotations=%5B%7B%22attribute%22%3A%22gene_chromosome_ensembl%22%7D%5D&filters=%5B%7B%22attribute%22%3A%22structure_data_existence_uniprot%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%221%22%7D%5D%7D%5D)
                    - target
                        - GlyTouCan
                    - filter
                        - Structure -> Proteins with structure data
                    - map
                        - Gene -> Chromosome
                    - comment
                        - 結果の数(1717)は表示されるが、20分経ってタイムアウトになる
                        - (3/16信定）高速化版で試行。数分で返ってくる。
                        - [http://ep.dbcls.jp/togodx-server-kohan-pg/build/?dataset=glytoucan&annotations=%5B%7B%22attribute%22%3A%22gene_chromosome_ensembl%22%7D%5D&filters=%5B%7B%22attribute%22%3A%22structure_data_existence_uniprot%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%221%22%7D%5D%7D%5D](http://ep.dbcls.jp/togodx-server-kohan-pg/build/?dataset=glytoucan&annotations=%5B%7B%22attribute%22%3A%22gene_chromosome_ensembl%22%7D%5D&filters=%5B%7B%22attribute%22%3A%22structure_data_existence_uniprot%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%221%22%7D%5D%7D%5D)
                        -
        - [リンク](http://ep.dbcls.jp/togodx-server-pg-dev/build/?dataset=glytoucan&annotations=%5B%7B%22attribute%22%3A%22gene_chromosome_ensembl%22%7D%5D&filters=%5B%7B%22attribute%22%3A%22structure_number_of_peptides_pdb%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%226%22%7D%5D%7D%5D)
            - target
                - GlyTouCan
            - filter
                - Structure -> # of peptides in a PDB entry
            - map
                - Gene -> Chromosome
            - comment
                - 結果の数(431)は表示されるが、20分経ってタイムアウトになる
                - (3/16信定）高速化版で試行。数十秒で返ってくる。
                - [http://ep.dbcls.jp/togodx-server-kohan-pg/build/?dataset=glytoucan&annotations=%5B%7B%22attribute%22%3A%22gene_chromosome_ensembl%22%7D%5D&filters=%5B%7B%22attribute%22%3A%22structure_number_of_peptides_pdb%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%226%22%7D%5D%7D%5D](http://ep.dbcls.jp/togodx-server-kohan-pg/build/?dataset=glytoucan&annotations=%5B%7B%22attribute%22%3A%22gene_chromosome_ensembl%22%7D%5D&filters=%5B%7B%22attribute%22%3A%22structure_number_of_peptides_pdb%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%226%22%7D%5D%7D%5D)
                -
        - [リンク](http://ep.dbcls.jp/togodx-server-pg-dev/build/?dataset=chebi&annotations=%5B%7B%22attribute%22%3A%22gene_chromosome_ensembl%22%7D%5D&filters=%5B%7B%22attribute%22%3A%22structure_number_of_beta_sheets_pdb%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%2214%22%7D%5D%7D%5D)
            - target
                - ChEBI/GlyTouCan
            - filter
                - Structure -> # of beta-sheets
            - map
                - Gene -> Chromosome
            - comment
                - 結果の数(10894/742)は表示されるが、20分経ってタイムアウトになる
                - (3/16信定）ChEBI：高速化版で試行。15分程度で返ってくる。が、その後重くて動かない（ページが応答しません）
                - ChEBI： [http://ep.dbcls.jp/togodx-server-kohan-pg/build/?dataset=chebi&annotations=%5B%7B%22attribute%22%3A%22gene_chromosome_ensembl%22%7D%5D&filters=%5B%7B%22attribute%22%3A%22structure_number_of_beta_sheets_pdb%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%2214%22%7D%5D%7D%5D](http://ep.dbcls.jp/togodx-server-kohan-pg/build/?dataset=chebi&annotations=%5B%7B%22attribute%22%3A%22gene_chromosome_ensembl%22%7D%5D&filters=%5B%7B%22attribute%22%3A%22structure_number_of_beta_sheets_pdb%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%2214%22%7D%5D%7D%5D)
                - (3/16信定）GlyTouCan：高速化版で試行。数十秒で返ってくる。
                - GlyTouCan：[http://ep.dbcls.jp/togodx-server-kohan-pg/build/?dataset=glytoucan&annotations=%5B%7B%22attribute%22%3A%22gene_chromosome_ensembl%22%7D%5D&filters=%5B%7B%22attribute%22%3A%22structure_number_of_beta_sheets_pdb%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%2214%22%7D%5D%7D%5D](http://ep.dbcls.jp/togodx-server-kohan-pg/build/?dataset=glytoucan&annotations=%5B%7B%22attribute%22%3A%22gene_chromosome_ensembl%22%7D%5D&filters=%5B%7B%22attribute%22%3A%22structure_number_of_beta_sheets_pdb%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%2214%22%7D%5D%7D%5D)
                -
        - [リンク](http://ep.dbcls.jp/togodx-server-pg-dev/build/?dataset=ensembl_gene&annotations=%5B%7B%22attribute%22%3A%22gene_chromosome_ensembl%22%7D%5D&filters=%5B%7B%22attribute%22%3A%22structure_analysis_methods_pdb%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%2204%22%7D%5D%7D%5D)
            - target
                - ENSG/NCBI Gene/UniProt/ChEBI/GlyTouCan/Mondo/MeSH
            - filter
                - Structure -> Analysis methods
            - map
                - Gene -> Chromosome
            - comment
                - 結果の数は表示されるが、20分経ってタイムアウトになる
                - (3/16信定）ENSG/NCBI Gene/UniProt/ChEBI/GlyTouCan/Mondo/MeSH：高速化版で試行。数秒~数分で返ってくる。59件/35件/74件/4510件/74件/23件/17件
                - ENSG: [http://ep.dbcls.jp/togodx-server-kohan-pg/build/?dataset=ensembl_gene&annotations=%5B%7B%22attribute%22%3A%22gene_chromosome_ensembl%22%7D%5D&filters=%5B%7B%22attribute%22%3A%22structure_analysis_methods_pdb%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%2204%22%7D%5D%7D%5D](http://ep.dbcls.jp/togodx-server-kohan-pg/build/?dataset=ensembl_gene&annotations=%5B%7B%22attribute%22%3A%22gene_chromosome_ensembl%22%7D%5D&filters=%5B%7B%22attribute%22%3A%22structure_analysis_methods_pdb%22%2C%22nodes%22%3A%5B%7B%22node%22%3A%2204%22%7D%5D%7D%5D)
                -