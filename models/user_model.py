from config.cmn_const import CmnConst
from models.cmn_model import CmnModel


class UserModel(CmnModel):

    def get_table(self):
        return "USER"

    def get_user_by_username_and_email(self, request):
        sql = (
            "SELECT "
            "  USER_ID, "
            "  USERNAME, "
            "  EMAIL "
            "FROM "
            "  USER "
            "WHERE "
            "  ( "
            "    USERNAME = %s OR "
            "    EMAIL = %s "
            "  ) AND "
            "  DELETE_FLG = %s"
        )

        params = [
            request["username"],
            request["email"],
            CmnConst.DELETE_FLG_OFF
        ]

        return self.query(sql, params)

    def count_content_of_user(self):
        sql = (
            "SELECT "
            "  COUNT(ct.ID) AS TOTAL_CONTENT, "
            "  u.USERNAME, "
            "  u.FULLNAME, "
            "  u.EMAIL, "
            "  u.AVATAR_TYPE "
            "FROM "
            "  USER AS u "
            "  LEFT JOIN CONTENT as ct ON "
            "    u.USER_ID = ct.USER_ID AND "
            "    u.DELETE_FLG = %s AND "
            "    ct.DELETE_FLG = %s "
            "GROUP BY "
            "  u.USERNAME, "
            "  u.FULLNAME, "
            "  u.EMAIL,"
            "  u.AVATAR_TYPE "
            "ORDER BY "
            "  TOTAL_CONTENT DESC"
        )

        params = [
            CmnConst.DELETE_FLG_OFF,
            CmnConst.DELETE_FLG_OFF
        ]

        return self.query(sql, params)
