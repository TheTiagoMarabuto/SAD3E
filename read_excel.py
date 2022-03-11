import xlrd


def read_graph_edges(sheet, edges, row_node, col_node):
    ncols = sheet.ncols
    nrows = sheet.nrows
    blank = ""
    if col_node > sheet.ncols - 1 or col_node < 0 or row_node > sheet.nrows - 1 or row_node < 0:
        print("Node coordinates in Excel are off limits")
        return

    node_name = sheet.cell_value(row_node, col_node)

    if not isinstance(node_name, str):
        print("Excel coordinates do not belong to a node")
        return

    if (row_node + 1) < nrows:
        if sheet.cell_value(row_node + 1, col_node) != blank:
            edges.append((node_name, sheet.cell_value(row_node + 2, col_node), sheet.cell_value(row_node + 1, col_node)))
    if (col_node + 1) < ncols:
        if sheet.cell_value(row_node, col_node + 1)!= blank:
            edges.append((node_name, sheet.cell_value(row_node, col_node + 2), sheet.cell_value(row_node, col_node + 1)))
    if (row_node - 2) > 0:
        if sheet.cell_value(row_node - 1, col_node)!= blank:
            edges.append((node_name, sheet.cell_value(row_node - 2, col_node), sheet.cell_value(row_node - 1, col_node)))
    if (col_node - 2) > 0:
        if sheet.cell_value(row_node, col_node - 1)!= blank:
            edges.append((node_name, sheet.cell_value(row_node, col_node - 2), sheet.cell_value(row_node, col_node - 1)))

    if (row_node + 1) < nrows and (col_node + 1) < ncols:
        if sheet.cell_value(row_node + 1, col_node + 1)!= blank:
            edges.append((node_name, sheet.cell_value(row_node + 2, col_node + 2), sheet.cell_value(row_node + 1, col_node + 1)))
    if (row_node + 1) < nrows and (col_node - 2) > 0:
        if sheet.cell_value(row_node + 1, col_node - 1)!= blank:
            edges.append((node_name, sheet.cell_value(row_node + 2, col_node - 2), sheet.cell_value(row_node + 1, col_node - 1)))
    if (row_node - 2) > 0 and (col_node + 1) < ncols:
        if sheet.cell_value(row_node - 1, col_node + 1)!= blank:
            edges.append((node_name, sheet.cell_value(row_node - 2, col_node + 2), sheet.cell_value(row_node - 1, col_node + 1)))
    if (row_node - 2) > 0 and (col_node - 2) > 0:
        if sheet.cell_value(row_node - 1, col_node - 1)!= blank:
            edges.append((node_name, sheet.cell_value(row_node - 2, col_node - 2), sheet.cell_value(row_node - 1, col_node - 1)))


def read_excel(sheet, edges):
    nrows = sheet.nrows
    ncols = sheet.ncols

    for i in range(nrows):
        for j in range(ncols):
            if (type(sheet.cell_value(j, i)) == str ) and (sheet.cell_value(j, i) != ""):
                read_graph_edges(sheet, edges, i, j)
