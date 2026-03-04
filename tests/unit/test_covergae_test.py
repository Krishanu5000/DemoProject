import unittest
from unittest.mock import patch
from pyspark.sql import SparkSession
from src.Spark_Practice.coverage_gen import AcosCovg


class AcosTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.spark = SparkSession.builder \
            .master("local[1]") \
            .appName("UnitTest") \
            .getOrCreate()

    def setUp(self):
        data = [(1, 100), (2, 200)]
        schema = ["acc_dim_id", "account_no"]

        self.account_df = self.spark.createDataFrame(data, schema)

        data = [("100G1", 100), ("200G2", 200)]
        schema = ["gwmidentifier", "externalaccountidentifier"]

        self.clnt_rel_roles_df = self.spark.createDataFrame(data, schema)
        self.clnt_rel_roles_df.show()

        data = [("2026-03-04", 10005, 1, '100G4'), ("2026-03-04", 10005, 2, '100G1'), ("2026-03-04", 10006, 3, '200G2')]
        schema = ["cycle_dt", "dmeciidentifier", "eciidentifier", "gwmidentifier"]

        self.party_core_df = self.spark.createDataFrame(data, schema)

        data = [("2026-03-04", 560, '100G1'), ("2026-03-04", 660, '200G2')]
        schema = ["cycle_dt", "organizationcode", "gwmidentifier"]

        self.clnt_covg_df = self.spark.createDataFrame(data, schema)

        data = [("2026-03-04", 560), ("2026-03-04", 660)]
        schema = ["cycle_dt", "org_id"]

        self.org_dim_df = self.spark.createDataFrame(data, schema)

        data = [(100, "100G1", "100G1", 2, 560), (200, "200G2", "200G2", 3, 660)]
        schema = ["account_no", "gwmidentifier", "dmgwmidentifier", "eciidentifier", "org_id"]
        self.expected_df = self.spark.createDataFrame(data, schema)
    @patch.object(SparkSession, "table")
    def test_transformation(self, mock_table):
        def table_side_effect(table_name):
            if table_name == "db_rft_radar_mart.account_dimension":
                return self.account_df

            elif table_name == "db_rft_radar_mart.client_rel_roles":
                return self.clnt_rel_roles_df

            elif table_name == "db_rft_radar_mart.party_core":
                return self.party_core_df

            elif table_name == "db_rft_radar_mart.clnt_covg":
                return self.clnt_covg_df

            elif table_name == "db_rft_radar_mart.organization_dimension":
                return self.org_dim_df

            else:
                raise ValueError("Unexpected table name")

        mock_table.side_effect = table_side_effect
        obj = AcosCovg
        self.actual_df = obj.transformation(self)
        self.actual_df.show()

        self.assertEqual(
            sorted(self.actual_df.collect()),
            sorted(self.expected_df.collect())
        )
