defmodule RNATranscription do
  @doc """
  Transcribes a character list representing DNA nucleotides to RNA

  ## Examples

  iex> RNATranscription.to_rna('ACTG')
  'UGAC'
  """
  @spec to_rna([char]) :: [char]
  def to_rna(dna) do
    # convert_dna_rna = fn
    #  65 -> {:ok, 'U'}
    #  67 -> {:ok, 'G'}
    #  84 -> {:ok, 'A'}
    #  71 -> {:ok, 'C'}
    #  _ -> {:fail, 'No Match'}
    # end

    res =
      Enum.each(dna, fn s ->
        s = ''
        'C'
      end)

    res
  end
end
