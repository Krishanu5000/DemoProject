from pyspark.sql import SparkSession
from pyspark.sql.functions import col, explode, avg, row_number
from pyspark.sql import Window


class AcosCovg:
    def __init__(self):
        self.spark = SparkSession.builder.getOrCreate()

    def transformation(self):
        account = self.spark.table("db_rft_radar_mart.account_dimension")
        clnt_rel_roles = self.spark.table("db_rft_radar_mart.client_rel_roles")
        party_core = self.spark.table("db_rft_radar_mart.party_core")
        clnt_covg = self.spark.table("db_rft_radar_mart.clnt_covg")
        org_dim = self.spark.table("db_rft_radar_mart.organization_dimension")

        w = Window.partitionBy(col("dmeciidentifier")).orderBy(col("eciidentifier").desc())
        part_core_unq = party_core.withColumn("rnum", row_number().over(w)).filter(col("rnum") == 1)

        part_core_unq.show()

        party_core_new = party_core.alias("a") \
            .join(part_core_unq.alias("b"), col("a.dmeciidentifier") == col("b.eciidentifier"), "inner") \
            .select(col("a.cycle_dt"), col("a.gwmidentifier"), col("b.gwmidentifier").alias("dmgwmidentifier"),
                    col("a.eciidentifier"))

        party_core_new.show()

        df = account.alias("acc") \
            .join(clnt_rel_roles.alias("rel_roles"),
                  col("acc.account_no") == col("rel_roles.externalaccountidentifier"), "left") \
            .join(party_core_new.alias("party"), col("party.gwmidentifier") == col("rel_roles.gwmidentifier"), "left") \
            # .join(clnt_covg.alias("covg"), col("party.dmgwmidentifier") == col("covg.gwmidentifier"), "left") \
        # .join(org_dim.alias("org"), col("covg.organizationcode") == col("org.org_id"), "left")

        # select_expr = [
        #     col("acc.account_no").alias("account_no"),
        #     col("party.gwmidentifier").alias("gwmidentifier"),
        #     col("party.dmgwmidentifier").alias("dmgwmidentifier"),
        #     col("party.eciidentifier").alias("eciidentifier"),
        #     col("org.org_id").alias("org_id")
        # ]
        #
        # df = df.select(*select_expr)
        df.show()
        return df
