# Implementation of matplotlib function 
import matplotlib.pyplot as plt 
  

  
fig = plt.figure()
ax = fig.add_subplot(111)
y = [1, 2, 3, 4, 5, 4, 3, 2, 1, 1, 1, 1, 1, 1, 1, 1]    
col_labels = ['Image-Name', 'IMG-SIZE', 'white PIXEL', 'BLACK PIXEL', 'GRAY_SHAP','img.dtype']
row_labels = ['1)', '2)', '3)', '4)', '5)','6)','7)','8)','9)','10)']
table_vals = [['IMG-MASKED-1',1689000,559122,112988,'(563, 1000)','uint8'],
              ['IMG-MASKED-2',2001000,666667,1334333,'(667, 1000)','uint8'], 
              ['IMG-MASKED-3', 2041308,671222,1370086,'(922, 738)','uint8'], 
              ['IMG-MASKED-4',2409480,803136,1606344,'(776, 1035)','uint8'], 
              ['IMG-MASKED-5',839040,279522,559518,'(368, 760)','uint8'],
              ['IMG-MASKED-6',2743296,914339,1828957,'(893, 1024)','uint8'],
              ['IMG-MASKED-7',386100,128689,257411,'(286, 450)','uint8'],
              ['IMG-MASKED-8', 4494000,1498000,2996000,'(1000, 1498)','uint8'],
              ['IMG-MASKED-9',151380,50380,101000,'(174, 290)','uint8'],
              ['IMG-MASKED-10',1995000,660559,1334441,'(665, 1000)','uint8']]
# Draw table
the_table = plt.table(cellText=table_vals,
                      colWidths=[0.1] * 6,
                      rowLabels=row_labels,
                      colLabels=col_labels,
                      loc='center')
the_table.auto_set_font_size(False)
the_table.set_fontsize(15)
the_table.scale(4, 3)

# Removing ticks and spines enables you to get the figure only with table
plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
plt.tick_params(axis='y', which='both', right=False, left=False, labelleft=False)
for pos in ['right','top','bottom','left']:
    plt.gca().spines[pos].set_visible(False)
       
  

plt.show()
