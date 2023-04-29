import xml.etree.ElementTree as ET
import sys
import math
import os


def convert_vpos(xml_file_path):
    """
    XMLファイルを読み込み、vposの値を変換する

    Args:
        xml_file_path (str): 変換したいXMLファイルのパス

    Returns:
        ElementTreeオブジェクト: vposの値が変換されたElementTreeオブジェクト
    """
    # XMLファイルをパースしてElementTreeオブジェクトを作成
    tree = ET.parse(xml_file_path)
    root = tree.getroot()

    # 一番最初の行のdateの値を基準として秒数に変換
    base_date = int(root[0].attrib['date'])
    base_date = math.floor(base_date / 10) * 10

    for chat in root:
        # vposの値を取得
        date = int(chat.attrib['date'])
        # dateの値を置換
        chat.set('vpos', str(int((date - base_date)*100)))

    return tree


def output_xml(tree, xml_file_path, prefix):
    """
    変換後のXMLをファイルに出力する

    Args:
        tree (ElementTreeオブジェクト): vposの値が変換されたElementTreeオブジェクト
        xml_file_path (str): 変換前のXMLファイルのパス
        prefix (str): 出力ファイル名に付ける接頭語

    Returns:
        None
    """
    # 変換後のXMLをファイルに出力
    xml_file_name = os.path.basename(xml_file_path)
    pre_xml_file_name = prefix + xml_file_name
    output_file_path = os.path.join(
        os.path.dirname(xml_file_path), pre_xml_file_name)

    tree.write(output_file_path, encoding='UTF-8', xml_declaration=True)
    print(f"Output file has been saved to: {output_file_path}")


if __name__ == '__main__':
    # 引数として渡されたファイルパスを取得
    if len(sys.argv) != 2:
        print("Usage: python program.py [XML file path]")
        sys.exit(1)
    xml_file_path = sys.argv[1]

    # 変換したいXMLファイルを読み込み、vposの値を変換
    tree = convert_vpos(xml_file_path)

    # 出力先のディレクトリとprefixを指定してXMLファイルを出力
    prefix = "output_"
    output_xml(tree, xml_file_path, prefix)
