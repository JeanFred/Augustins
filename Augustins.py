# -*- coding: latin-1 -*-

"""Partnership with the MHNT."""

__authors__ = 'User:Jean-Frédéric'

import os
import sys
from uploadlibrary import metadata
from uploadlibrary.UploadBot import DataIngestionBot, UploadBotArgumentParser
reload(sys)
sys.setdefaultencoding('utf-8')


class AugustinsMetadataCollection(metadata.MetadataCollection):

    """Handling the metadata collection."""

    def handle_record(self, image_metadata):
        """Handle a record."""
        filename = image_metadata['REF IMAGE']
        #path = os.path.abspath(os.path.join('.', 'images', filename))
        return metadata.MetadataRecord(filename, image_metadata)


def main(args):
    """Main method."""
    collection = AugustinsMetadataCollection()
    csv_file = 'AugustinsMetadata.csv'
    collection.retrieve_metadata_from_csv(csv_file, delimiter=';')

    alignment_template = 'User:Jean-Frédéric/AlignmentRow'.encode('utf-8')

    if args.prepare_alignment:
        for key, value in collection.count_metadata_values().items():
            collection.write_dict_as_wiki(value, key, 'wiki',
                                          alignment_template)

    if args.post_process:
        mapping_fields = ['ARTSIT', 'DATE', 'MEDIUM']
        collection.retrieve_metadata_alignments(mapping_fields,
                                                alignment_template)

        #reader = collection.post_process_collection(mapping)
        template_name = 'Commons:Musée des Augustins/Ingestion'.encode('utf-8')
        front_titlefmt = ""
        variable_titlefmt = "%(ARTIST)s - %(TITLE)s"
        rear_titlefmt = " - Musée des Augustins - %(ACCESSION NUMBER)s"
        uploadBot = DataIngestionBot(reader=iter(collection.records),
                                     front_titlefmt=front_titlefmt,
                                     rear_titlefmt=rear_titlefmt,
                                     variable_titlefmt=variable_titlefmt,
                                     pagefmt=template_name)

    if args.upload:
        uploadBot.doSingle()
    elif args.dry_run:
        uploadBot.dry_run()


if __name__ == "__main__":
    parser = UploadBotArgumentParser()
    arguments = parser.parse_args()
    main(arguments)
