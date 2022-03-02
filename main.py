"""
This DocumentCloud Add-On allows you to bulk edit documents
"""

from documentcloud.toolbox import grouper

from addon import AddOn

BULK_LIMIT = 25


class BulkEdit(AddOn):
    """Bulk edit DocumentCloud documents"""

    def main(self):

        attrs = ["source", "description", "related_article", "published_url"]
        data = {a: self.data[a] for a in attrs if a in self.data}

        # fetch 25 documents at a time, and bulk edit them in one call
        documents = self.client.documents.search(self.query, per_page=BULK_LIMIT)
        for page_documents in grouper(documents, BULK_LIMIT):
            response = self.client.patch(
                "documents/", json=[{"id": d.id, **data} for d in page_documents]
            )


if __name__ == "__main__":
    BulkEdit().main()
